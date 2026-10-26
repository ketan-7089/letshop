import boto3
import time
import base64
import urllib.request

REGION = 'ap-south-1'
RDS_ID = 'lab9-db'
DB_PASSWORD = 'Lab9Pass2026'
WEB_SG_ID = 'sg-0ca9e9282a2e5acb6'
TG_ARN = 'arn:aws:elasticloadbalancing:ap-south-1:275839157944:targetgroup/lab9-tg/9e411e9566ae6116'
ALB_DNS = 'lab9-alb-1124916963.ap-south-1.elb.amazonaws.com'
SUBNET_IDS = 'subnet-002d68eb5e123e06f,subnet-06413db64463c2f4c,subnet-079f53e3803c540be'
AMI_ID = 'ami-022374b883d9d7931' # Amazon Linux 2023 x86_64

rds = boto3.client('rds', region_name=REGION)
ec2 = boto3.client('ec2', region_name=REGION)
asg = boto3.client('autoscaling', region_name=REGION)
elbv2 = boto3.client('elbv2', region_name=REGION)

print("[*] Waiting for RDS instance to be available...")
while True:
    db = rds.describe_db_instances(DBInstanceIdentifier=RDS_ID)['DBInstances'][0]
    status = db['DBInstanceStatus']
    print(f"    RDS Status: {status}")
    if status == 'available':
        endpoint = db['Endpoint']['Address']
        print(f"[+] RDS is Available! Endpoint: {endpoint}")
        break
    time.sleep(15)

# Step 3: Create Launch Template
print("[*] Creating Launch Template: lab9-web-template...")
user_data_script = f"""#!/bin/bash
dnf install -y httpd php php-fpm php-mysqli
systemctl enable --now httpd php-fpm
echo OK > /var/www/html/health.html
cat > /var/www/html/load.php << 'EOF'
<?php
$end = microtime(true) + 0.3;
while (microtime(true) < $end) {{ sqrt(mt_rand()); }}
echo 'load done';
EOF
cat > /var/www/html/index.php << 'EOF'
<?php
$t = shell_exec('curl -s -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 60"');
$id = trim(shell_exec('curl -s -H "X-aws-ec2-metadata-token: '.$t.'" http://169.254.169.254/latest/meta-data/instance-id'));
$az = trim(shell_exec('curl -s -H "X-aws-ec2-metadata-token: '.$t.'" http://169.254.169.254/latest/meta-data/placement/availability-zone'));
echo '<h1>AWS Auto Scaling Lab - Experiment 9</h1>';
echo '<p><b>Served by instance:</b> '.$id.'</p>';
echo '<p><b>Availability Zone:</b> '.$az.'</p>';
mysqli_report(MYSQLI_REPORT_OFF);
$c = @new mysqli('{endpoint}', 'admin', '{DB_PASSWORD}', 'labdb');
if ($c->connect_errno) {{
 echo '<p style="color:red"><b>Database:</b> not connected yet (refresh in a minute)</p>';
}} else {{
 $c->query('CREATE TABLE IF NOT EXISTS visits (id INT AUTO_INCREMENT PRIMARY KEY, instance VARCHAR(30), ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP)');
 $c->query("INSERT INTO visits (instance) VALUES ('".$id."')");
 $r = $c->query('SELECT COUNT(*) AS n FROM visits')->fetch_assoc();
 echo '<p style="color:green"><b>Database:</b> connected. Total visits stored in RDS: '.$r['n'].'</p>';
}}
EOF
chown -R apache:apache /var/www/html
"""

user_data_b64 = base64.b64encode(user_data_script.encode('utf-8')).decode('utf-8')

try:
    # Delete older template if exists
    try:
        ec2.delete_launch_template(LaunchTemplateName='lab9-web-template')
    except Exception:
        pass

    lt_res = ec2.create_launch_template(
        LaunchTemplateName='lab9-web-template',
        LaunchTemplateData={
            'ImageId': AMI_ID,
            'InstanceType': 't3.micro',
            'SecurityGroupIds': [WEB_SG_ID],
            'UserData': user_data_b64,
            'Monitoring': {'Enabled': True},
            'MetadataOptions': {
                'HttpTokens': 'optional',
                'HttpPutResponseHopLimit': 2,
                'HttpEndpoint': 'enabled'
            }
        }
    )
    print(f"[+] Launch template created! ID: {lt_res['LaunchTemplate']['LaunchTemplateId']}")
except Exception as e:
    print(f"[-] Error creating launch template: {e}")

# Step 6: Create Auto Scaling Group
print("[*] Creating Auto Scaling Group: lab9-asg...")
try:
    try:
        asg.delete_auto_scaling_group(AutoScalingGroupName='lab9-asg', ForceDelete=True)
        time.sleep(5)
    except Exception:
        pass

    asg.create_auto_scaling_group(
        AutoScalingGroupName='lab9-asg',
        LaunchTemplate={'LaunchTemplateName': 'lab9-web-template', 'Version': '$Default'},
        MinSize=2,
        MaxSize=4,
        DesiredCapacity=2,
        DefaultCooldown=60,
        VPCZoneIdentifier=SUBNET_IDS,
        TargetGroupARNs=[TG_ARN],
        HealthCheckType='ELB',
        HealthCheckGracePeriod=180
    )
    print("[+] Auto Scaling Group created successfully!")

    # Attach Target Tracking Scaling Policy
    print("[*] Creating Target Tracking Policy (CPU 50%)...")
    policy_res = asg.put_scaling_policy(
        AutoScalingGroupName='lab9-asg',
        PolicyName='cpu50-target-tracking',
        PolicyType='TargetTrackingScaling',
        TargetTrackingConfiguration={
            'PredefinedMetricSpecification': {'PredefinedMetricType': 'ASGAverageCPUUtilization'},
            'TargetValue': 50.0,
            'EstimatedInstanceWarmup': 60
        }
    )
    print(f"[+] Scaling policy attached! ARN: {policy_res['PolicyARN']}")
except Exception as e:
    print(f"[-] Error configuring ASG: {e}")

# Wait for 2 healthy targets
print("[*] Waiting for 2 instances to show Healthy in Target Group (approx 3-4 mins)...")
while True:
    th = elbv2.describe_target_health(TargetGroupArn=TG_ARN)['TargetHealthDescriptions']
    healthy_count = sum(1 for t in th if t['TargetHealth']['State'] == 'healthy')
    print(f"    Current targets: {len(th)} | Healthy: {healthy_count}")
    if healthy_count >= 2:
        print("[+] 2 Targets are Healthy!")
        break
    time.sleep(15)

print("\n" + "="*60)
print(f"[*] Testing ALB endpoint: http://{ALB_DNS}")
for i in range(5):
    try:
        with urllib.request.urlopen(f"http://{ALB_DNS}", timeout=5) as resp:
            content = resp.read().decode('utf-8', errors='ignore')
            clean_content = content.replace('<h1>', '').replace('</h1>', '').replace('<p>', '').replace('</p>', ' | ')
            print(f"Hit {i+1}: {clean_content.strip()}")
    except Exception as e:
        print(f"Hit {i+1} failed: {e}")
    time.sleep(1)

print("\n[+] Setup complete and verified!")
