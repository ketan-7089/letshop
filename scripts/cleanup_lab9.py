import boto3
import time

REGION = 'ap-south-1'
asg = boto3.client('autoscaling', region_name=REGION)
ec2 = boto3.client('ec2', region_name=REGION)
elbv2 = boto3.client('elbv2', region_name=REGION)
rds = boto3.client('rds', region_name=REGION)

print("[*] Starting Clean-up of Lab 9 resources in ap-south-1...")

# 1. Delete Auto Scaling Group
print("\n[1/5] Deleting Auto Scaling Group: lab9-asg...")
try:
    # Set capacity to 0 to accelerate termination
    asg.update_auto_scaling_group(
        AutoScalingGroupName='lab9-asg',
        MinSize=0,
        DesiredCapacity=0
    )
    asg.delete_auto_scaling_group(AutoScalingGroupName='lab9-asg', ForceDelete=True)
    print("    ASG deletion initiated. Waiting for all ASG instances to terminate...")
    while True:
        res = asg.describe_auto_scaling_groups(AutoScalingGroupNames=['lab9-asg'])['AutoScalingGroups']
        if not res or len(res[0]['Instances']) == 0:
            print("    [+] ASG instances completely terminated and removed!")
            break
        print(f"    Waiting... Remaining instances: {len(res[0]['Instances'])}")
        time.sleep(10)
except Exception as e:
    print(f"    ASG clean-up notice: {e}")

# 2. Delete Load Balancer and Target Group
print("\n[2/5] Deleting Load Balancer: lab9-alb and Target Group: lab9-tg...")
try:
    albs = elbv2.describe_load_balancers(Names=['lab9-alb'])['LoadBalancers']
    if albs:
        alb_arn = albs[0]['LoadBalancerArn']
        elbv2.delete_load_balancer(LoadBalancerArn=alb_arn)
        print("    [+] ALB lab9-alb deleted!")
        print("    Waiting for ALB to release network interfaces (approx 30s)...")
        time.sleep(30)
except Exception as e:
    print(f"    ALB notice: {e}")

try:
    tgs = elbv2.describe_target_groups(Names=['lab9-tg'])['TargetGroups']
    if tgs:
        tg_arn = tgs[0]['TargetGroupArn']
        elbv2.delete_target_group(TargetGroupArn=tg_arn)
        print("    [+] Target Group lab9-tg deleted!")
except Exception as e:
    print(f"    Target Group notice: {e}")

# 3. Delete Launch Template
print("\n[3/5] Deleting Launch Template: lab9-web-template...")
try:
    ec2.delete_launch_template(LaunchTemplateName='lab9-web-template')
    print("    [+] Launch Template lab9-web-template deleted!")
except Exception as e:
    print(f"    Launch Template notice: {e}")

# 4. Delete RDS Database
print("\n[4/5] Deleting RDS Database: lab9-db...")
try:
    dbs = rds.describe_db_instances(DBInstanceIdentifier='lab9-db')['DBInstances']
    if dbs:
        status = dbs[0]['DBInstanceStatus']
        if status != 'deleting':
            rds.delete_db_instance(
                DBInstanceIdentifier='lab9-db',
                SkipFinalSnapshot=True,
                DeleteAutomatedBackups=True
            )
            print("    [+] RDS lab9-db deletion initiated with SkipFinalSnapshot=True!")
        else:
            print("    RDS lab9-db is already in deleting state.")
except Exception as e:
    print(f"    RDS notice: {e}")

# Wait for instances to fully transition to 'terminated' state before deleting security groups
print("\n[5/5] Cleaning up Security Groups: db-sg, web-sg, alb-sg...")
print("    Waiting for EC2 instances and RDS to release security group dependencies...")
for attempt in range(12):
    try:
        # Check security groups
        sgs = ec2.describe_security_groups()['SecurityGroups']
        sg_dict = {s['GroupName']: s['GroupId'] for s in sgs}
        
        # Delete db-sg
        if 'db-sg' in sg_dict:
            try:
                ec2.delete_security_group(GroupId=sg_dict['db-sg'])
                print("    [+] db-sg deleted!")
            except Exception as e:
                pass

        # Delete web-sg
        if 'web-sg' in sg_dict:
            try:
                ec2.delete_security_group(GroupId=sg_dict['web-sg'])
                print("    [+] web-sg deleted!")
            except Exception as e:
                pass

        # Delete alb-sg
        if 'alb-sg' in sg_dict:
            try:
                ec2.delete_security_group(GroupId=sg_dict['alb-sg'])
                print("    [+] alb-sg deleted!")
            except Exception as e:
                pass

        # If all 3 are gone, break
        sgs = ec2.describe_security_groups()['SecurityGroups']
        remaining = [s['GroupName'] for s in sgs if s['GroupName'] in ['alb-sg', 'web-sg', 'db-sg']]
        if not remaining:
            print("    [+] All 3 lab security groups successfully deleted!")
            break
        print(f"    Attempt {attempt+1}/12: Waiting on remaining SGs ({remaining})...")
        time.sleep(15)
    except Exception as e:
        time.sleep(15)

print("\n[+] Clean-up routine finished!")
