import urllib.request
import threading
import time
import boto3
from datetime import datetime, timezone

REGION = 'ap-south-1'
ALB_DNS = 'lab9-alb-1124916963.ap-south-1.elb.amazonaws.com'
LOAD_URL = f"http://{ALB_DNS}/load.php"

asg = boto3.client('autoscaling', region_name=REGION)
cw = boto3.client('cloudwatch', region_name=REGION)
elbv2 = boto3.client('elbv2', region_name=REGION)
TG_ARN = 'arn:aws:elasticloadbalancing:ap-south-1:275839157944:targetgroup/lab9-tg/9e411e9566ae6116'

stop_flag = False

def worker():
    while not stop_flag:
        try:
            req = urllib.request.Request(LOAD_URL, headers={'User-Agent': 'LoadTester/1.0'})
            with urllib.request.urlopen(req, timeout=3) as resp:
                resp.read()
        except Exception:
            pass

print(f"[*] Starting Load Test against {LOAD_URL} at {datetime.now(timezone.utc).isoformat()}...")
threads = []
for i in range(40):
    t = threading.Thread(target=worker, daemon=True)
    t.start()
    threads.append(t)

print(f"[+] 40 concurrent workers launched. Monitoring ASG and CloudWatch for 5 minutes...")

start_time = time.time()
while time.time() - start_time < 300: # 5 minutes
    # Check ASG activity
    activities = asg.describe_scaling_activities(AutoScalingGroupName='lab9-asg', MaxRecords=5)['Activities']
    latest_activity = activities[0]['Description'] if activities else "None"
    
    # Check ASG group size
    group = asg.describe_auto_scaling_groups(AutoScalingGroupNames=['lab9-asg'])['AutoScalingGroups'][0]
    instances = len(group['Instances'])
    desired = group['DesiredCapacity']
    
    # Check Target health
    th = elbv2.describe_target_health(TargetGroupArn=TG_ARN)['TargetHealthDescriptions']
    healthy_targets = sum(1 for t in th if t['TargetHealth']['State'] == 'healthy')
    
    # Check CloudWatch Alarms
    alarms = cw.describe_alarms(AlarmNamePrefix='TargetTracking-lab9-asg-AlarmHigh')['MetricAlarms']
    alarm_state = alarms[0]['StateValue'] if alarms else "UNKNOWN"
    
    elapsed = int(time.time() - start_time)
    print(f"[{elapsed}s] Alarm: {alarm_state} | Desired: {desired} | Instances: {instances} | Healthy Targets: {healthy_targets} | Latest Activity: {latest_activity[:60]}...")
    
    if instances >= 4 and healthy_targets >= 4:
        print("[+] Reached 4 healthy instances! Scaling out successfully observed!")
        break
        
    time.sleep(20)

stop_flag = True
print("[*] Load test phase completed. Stopping workers...")
time.sleep(5)
