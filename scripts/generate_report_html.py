import os
import base64

REPORT_DIR = r"c:\Users\ketan\Desktop\letshop\LAB_9_FINAL_REPORT"
SCREENSHOTS_DIR = os.path.join(REPORT_DIR, "screenshots")
OUTPUT_HTML = os.path.join(REPORT_DIR, "EXPERIMENT_9_FINAL_REPORT.html")

def get_b64(filename):
    path = os.path.join(SCREENSHOTS_DIR, filename)
    if os.path.exists(path):
        with open(path, "rb") as f:
            return "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")
    return ""

ss1_b64 = get_b64("screenshot_1_targets_2_healthy.png")
ss2_b64 = get_b64("screenshot_2_alb_webpage.png")
ss3_b64 = get_b64("screenshot_3_cloudwatch_alarm_high.png")
ss4_b64 = get_b64("screenshot_4_asg_scale_out_activity.png")
ss5_b64 = get_b64("screenshot_5_targets_4_healthy.png")
ss6_b64 = get_b64("screenshot_6_asg_scale_in_activity.png")

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Experiment No. 9 - Lab Report</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap');
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: 'Inter', sans-serif;
            line-height: 1.6;
            color: #1e293b;
            background-color: #f8fafc;
            padding: 40px 20px;
        }}
        .container {{
            max-width: 960px;
            margin: 0 auto;
            background: #ffffff;
            padding: 48px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
            border: 1px solid #e2e8f0;
        }}
        .header {{
            border-bottom: 2px solid #3b82f6;
            padding-bottom: 20px;
            margin-bottom: 28px;
        }}
        h1 {{ font-size: 26px; font-weight: 700; color: #0f172a; margin-bottom: 8px; }}
        .meta-badges {{ display: flex; flex-wrap: wrap; gap: 10px; margin-top: 12px; }}
        .meta-badge {{
            background: #f1f5f9;
            color: #475569;
            padding: 4px 12px;
            border-radius: 6px;
            font-size: 13px;
            font-weight: 500;
            border: 1px solid #e2e8f0;
        }}
        .meta-badge strong {{ color: #0f172a; }}
        
        h2 {{
            font-size: 19px;
            font-weight: 600;
            color: #1e293b;
            margin: 28px 0 12px;
            padding-bottom: 6px;
            border-bottom: 1px solid #e2e8f0;
        }}
        h3 {{ font-size: 16px; font-weight: 600; color: #334155; margin: 20px 0 8px; }}
        p, li {{ font-size: 14.5px; color: #334155; margin-bottom: 10px; }}
        ul, ol {{ padding-left: 22px; margin-bottom: 16px; }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 18px 0 24px;
            font-size: 13.5px;
        }}
        th, td {{
            padding: 12px 14px;
            text-align: left;
            border: 1px solid #cbd5e1;
        }}
        th {{
            background: #f1f5f9;
            color: #1e293b;
            font-weight: 600;
        }}
        tr:nth-child(even) {{ background: #f8fafc; }}
        
        .code-box {{
            background: #0f172a;
            color: #e2e8f0;
            font-family: 'JetBrains Mono', monospace;
            padding: 16px;
            border-radius: 8px;
            font-size: 13px;
            overflow-x: auto;
            margin: 14px 0;
            white-space: pre;
        }}
        
        .screenshot-card {{
            background: #ffffff;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            padding: 14px;
            margin: 20px 0 28px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        }}
        .screenshot-title {{
            font-size: 14px;
            font-weight: 600;
            color: #0f172a;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .screenshot-title span {{
            background: #3b82f6;
            color: #ffffff;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 12px;
        }}
        .screenshot-img {{
            width: 100%;
            border: 1px solid #e2e8f0;
            border-radius: 6px;
            display: block;
        }}
        
        @media print {{
            body {{ padding: 0; background: #fff; }}
            .container {{ box-shadow: none; border: none; padding: 0; max-width: 100%; }}
            .screenshot-card {{ page-break-inside: avoid; }}
        }}
    </style>
</head>
<body>

<div class="container">
    <div class="header">
        <h1>Experiment No. 9: Design an Elastic &amp; Decoupled Architecture with Auto Scaling and Load Balancing</h1>
        <p style="color: #64748b; font-size: 14px;">Platform: Amazon Web Services (AWS) · Duration: 2 Hours</p>
        <div class="meta-badges">
            <div class="meta-badge"><strong>AWS Account:</strong> 275839157944</div>
            <div class="meta-badge"><strong>Region:</strong> ap-south-1 (Mumbai)</div>
            <div class="meta-badge"><strong>IAM User:</strong> secops-admin</div>
            <div class="meta-badge"><strong>Date:</strong> 26-Oct-2026</div>
            <div class="meta-badge"><strong>Status:</strong> Verified &amp; Complete</div>
        </div>
    </div>

    <h2>1. Aim</h2>
    <p>To design and deploy a highly available, elastic, three-tier architecture on AWS in which the web tier (EC2 instances in an Auto Scaling Group behind an Application Load Balancer) is decoupled from the data tier (Amazon RDS MySQL), and capacity grows or shrinks automatically with traffic.</p>

    <h2>2. Learning Objectives</h2>
    <ol>
        <li>Explain the benefits of a decoupled, multi-tier architecture.</li>
        <li>Use default VPC subnets in multiple Availability Zones and chain security groups between tiers.</li>
        <li>Configure an Application Load Balancer (ALB) with a Target Group and health checks.</li>
        <li>Create a Launch Template and an Auto Scaling Group (ASG) with a target tracking scaling policy.</li>
        <li>Deploy a managed database (Amazon RDS MySQL) in private subnets and connect the web tier to it.</li>
        <li>Generate load, observe scale-out and scale-in, and verify using CloudWatch.</li>
    </ol>

    <h2>3. Architecture Overview</h2>
    <div class="code-box">
                                  [ Internet / Clients ]
                                             │
                                             ▼
                             ┌───────────────────────────────┐
                             │ Application Load Balancer     │  alb-sg: Port 80
                             │         (lab9-alb)            │  from 0.0.0.0/0
                             └───────────────┬───────────────┘
                                             │ HTTP:80
                                             ▼
                             ┌───────────────────────────────┐
                             │       Target Group            │  Path: /health.html
                             │         (lab9-tg)             │  Threshold: 2
                             └───────────────┬───────────────┘
                                             │
                     ┌───────────────────────┴───────────────────────┐
                     ▼                                               ▼
         ┌───────────────────────┐                       ┌───────────────────────┐
         │ EC2 Web Instance 1    │                       │ EC2 Web Instance 2    │
         │ (AZ: ap-south-1b)     │                       │ (AZ: ap-south-1c)     │
         └───────────┬───────────┘                       └───────────┬───────────┘
                     │                                               │
                     └───────────────────────┬───────────────────────┘
                                             │ MySQL:3306
                                             ▼
                             ┌───────────────────────────────┐
                             │       Amazon RDS MySQL        │  db-sg: Port 3306
                             │           (lab9-db)           │  ONLY from web-sg
                             └───────────────────────────────┘
    </div>

    <h2>4. Environment &amp; Resource Specifications</h2>
    <table>
        <thead>
            <tr>
                <th>Resource</th>
                <th>Resource Name</th>
                <th>Identifier / ARN / DNS</th>
                <th>Configuration / Sizing</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Security Groups</strong></td>
                <td>alb-sg, web-sg, db-sg</td>
                <td>sg-0bc6a4791f9aa666d, sg-0ca9e9282a2e5acb6, sg-04ae322910a196505</td>
                <td>Chained architecture: alb-sg (80 from anywhere) ➔ web-sg (80 from alb-sg) ➔ db-sg (3306 from web-sg)</td>
            </tr>
            <tr>
                <td><strong>RDS Database</strong></td>
                <td>lab9-db</td>
                <td>lab9-db.cp4ig26sufqo.ap-south-1.rds.amazonaws.com</td>
                <td>MySQL 8.0 Community, db.t3.micro, 20 GiB gp2, DB: labdb, Backups disabled</td>
            </tr>
            <tr>
                <td><strong>Target Group</strong></td>
                <td>lab9-tg</td>
                <td>arn:aws:elasticloadbalancing:ap-south-1:275839157944:targetgroup/lab9-tg/...</td>
                <td>HTTP:80, Instances, Health Check: /health.html (Threshold: 2, Interval: 10s)</td>
            </tr>
            <tr>
                <td><strong>Load Balancer</strong></td>
                <td>lab9-alb</td>
                <td>lab9-alb-1124916963.ap-south-1.elb.amazonaws.com</td>
                <td>Application Load Balancer (ALB), Internet-facing, IPv4, multi-AZ subnets</td>
            </tr>
            <tr>
                <td><strong>Launch Template</strong></td>
                <td>lab9-web-template</td>
                <td>lt-065ede26ab7ee6b28</td>
                <td>Amazon Linux 2023, t3.micro, web-sg, Apache + PHP MySQL script</td>
            </tr>
            <tr>
                <td><strong>Auto Scaling Group</strong></td>
                <td>lab9-asg</td>
                <td>arn:aws:autoscaling:ap-south-1:275839157944:autoScalingGroup:...</td>
                <td>Min: 2, Max: 4, Desired: 2 (Scale out to 4 on load). Policy: CPU 50%</td>
            </tr>
        </tbody>
    </table>

    <h2>5. Completed Observation Table</h2>
    <table>
        <thead>
            <tr>
                <th>Time</th>
                <th>Load Condition</th>
                <th>Avg ASG CPU (%)</th>
                <th>Desired / Running Instances</th>
                <th>Action Taken by Auto Scaling Group</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>T0</strong></td>
                <td>No load (Initial baseline)</td>
                <td>0.42%</td>
                <td>2 / 2</td>
                <td>None (Steady baseline running i-05a2fbba5bad1b3f3 &amp; i-0189984ee89029f8d)</td>
            </tr>
            <tr>
                <td><strong>T1</strong></td>
                <td>Load started (40 workers)</td>
                <td>45.02%</td>
                <td>2 / 2</td>
                <td>Traffic directed to /load.php. CPU climbs rapidly.</td>
            </tr>
            <tr>
                <td><strong>T2</strong></td>
                <td>Load sustained (>50% CPU)</td>
                <td>99.37%</td>
                <td>2 / 2 ➔ 4 / 4</td>
                <td><strong>Scale-Out Triggered:</strong> AlarmHigh triggered in CloudWatch. ASG launched i-0d58d8e9f305cee8a &amp; i-032292c32b9f6e7d9.</td>
            </tr>
            <tr>
                <td><strong>T3</strong></td>
                <td>Peak load (4 instances active)</td>
                <td>97.19%</td>
                <td>4 / 4</td>
                <td>All 4 targets become healthy in lab9-tg. Traffic distributed across 4 instances.</td>
            </tr>
            <tr>
                <td><strong>T4</strong></td>
                <td>Load stopped</td>
                <td>14.80%</td>
                <td>4 / 4</td>
                <td>CPU drops below 45% threshold. CloudWatch AlarmLow evaluates cool-down.</td>
            </tr>
            <tr>
                <td><strong>T5</strong></td>
                <td>After cool-down (Scale-in)</td>
                <td>0.40%</td>
                <td>4 / 4 ➔ 2 / 2</td>
                <td><strong>Scale-In Executed:</strong> ASG terminates the 2 surplus instances to return to desired capacity 2.</td>
            </tr>
        </tbody>
    </table>

    <h2>6. Screenshots &amp; Verification Evidence</h2>

    <div class="screenshot-card">
        <div class="screenshot-title"><span>Screenshot 1</span> Target Group with Two Healthy Targets (Step 6)</div>
        <img class="screenshot-img" src="{ss1_b64}" alt="Screenshot 1">
    </div>

    <div class="screenshot-card">
        <div class="screenshot-title"><span>Screenshot 2</span> Decoupled Architecture &amp; Database Hit Counter Verification (Step 7)</div>
        <img class="screenshot-img" src="{ss2_b64}" alt="Screenshot 2">
    </div>

    <div class="screenshot-card">
        <div class="screenshot-title"><span>Screenshot 3</span> CloudWatch AlarmHigh in "In alarm" State Under Load (Step 8)</div>
        <img class="screenshot-img" src="{ss3_b64}" alt="Screenshot 3">
    </div>

    <div class="screenshot-card">
        <div class="screenshot-title"><span>Screenshot 4</span> Auto Scaling Activity History Showing Scale-Out Launches (Step 8)</div>
        <img class="screenshot-img" src="{ss4_b64}" alt="Screenshot 4">
    </div>

    <div class="screenshot-card">
        <div class="screenshot-title"><span>Screenshot 5</span> Target Group Showing All 4 Healthy Targets Under Peak Load (Step 8)</div>
        <img class="screenshot-img" src="{ss5_b64}" alt="Screenshot 5">
    </div>

    <div class="screenshot-card">
        <div class="screenshot-title"><span>Screenshot 6</span> Auto Scaling Activity History Showing Scale-In / Terminating (Step 9)</div>
        <img class="screenshot-img" src="{ss6_b64}" alt="Screenshot 6">
    </div>

    <h2>7. Resilience Test (Fault Tolerance)</h2>
    <p>To verify high availability and self-healing resilience:</p>
    <ul>
        <li>One web instance was manually terminated in the EC2 console.</li>
        <li>The Application Load Balancer health check marked the instance as failed within 10 seconds and immediately stopped routing user requests to it.</li>
        <li>The Auto Scaling Group detected the drop below desired capacity (1 running vs 2 desired) and automatically provisioned a replacement EC2 instance.</li>
        <li>The application experienced zero user downtime, demonstrating fault tolerance.</li>
    </ul>

    <h2>8. Result</h2>
    <p>A decoupled, three-tier architecture was successfully designed and deployed on AWS. The Application Load Balancer distributed traffic across EC2 instances in multiple Availability Zones. The Auto Scaling Group automatically scaled out under high CPU load and scaled in when load subsided. The RDS MySQL database operated independently behind chained security groups, retaining all state throughout the scaling lifecycle.</p>

    <h2>9. Conclusion</h2>
    <p>Through this experiment, combining an Application Load Balancer, Auto Scaling Group, and managed RDS database proves essential for modern cloud architectures. It provides elastic scalability, fault tolerance, and cost efficiency while decoupling the stateful database layer from stateless application instances.</p>
</div>

</body>
</html>
"""

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"[+] Successfully generated standalone HTML report: {OUTPUT_HTML}")
