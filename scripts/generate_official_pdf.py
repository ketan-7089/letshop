import os
import base64
import subprocess

REPORT_DIR = r"c:\Users\ketan\Desktop\letshop\LAB_9_FINAL_REPORT"
SCREENSHOTS_DIR = os.path.join(REPORT_DIR, "screenshots")
HTML_FILE = os.path.join(REPORT_DIR, "report_for_pdf.html")
PDF_FILE = os.path.join(REPORT_DIR, "Experiment_9_AWS_AutoScaling_Decoupled_Lab_Report.pdf")
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

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

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Experiment No. 9 - AWS Elastic & Decoupled Architecture Lab Report</title>
<style>
    @page {{
        size: A4;
        margin: 14mm 15mm 14mm 15mm;
    }}
    * {{
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif;
    }}
    body {{
        color: #1e293b;
        background: #fff;
        font-size: 10.5pt;
        line-height: 1.5;
    }}
    .header-box {{
        border-bottom: 2.5px solid #2563eb;
        padding-bottom: 12px;
        margin-bottom: 18px;
    }}
    .exp-title {{
        font-size: 18pt;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 4px;
    }}
    .exp-subtitle {{
        font-size: 12pt;
        font-weight: 600;
        color: #2563eb;
        margin-bottom: 8px;
    }}
    .meta-table {{
        width: 100%;
        border-collapse: collapse;
        margin-top: 8px;
        font-size: 9.5pt;
    }}
    .meta-table td {{
        padding: 4px 8px;
        border: 1px solid #e2e8f0;
        background: #f8fafc;
    }}
    .meta-table td strong {{
        color: #0f172a;
    }}
    h2 {{
        font-size: 13pt;
        font-weight: 700;
        color: #0f172a;
        margin-top: 18px;
        margin-bottom: 8px;
        border-left: 4px solid #2563eb;
        padding-left: 8px;
    }}
    h3 {{
        font-size: 11pt;
        font-weight: 600;
        color: #1e293b;
        margin-top: 14px;
        margin-bottom: 4px;
    }}
    p, li {{
        font-size: 10pt;
        color: #334155;
        margin-bottom: 4px;
        text-align: justify;
    }}
    ul, ol {{
        padding-left: 20px;
        margin-bottom: 10px;
    }}
    table.data-table {{
        width: 100%;
        border-collapse: collapse;
        margin: 12px 0 16px;
        font-size: 9.5pt;
    }}
    table.data-table th, table.data-table td {{
        padding: 7px 10px;
        border: 1px solid #cbd5e1;
        text-align: left;
    }}
    table.data-table th {{
        background: #f1f5f9;
        color: #0f172a;
        font-weight: 600;
    }}
    table.data-table tr:nth-child(even) {{
        background: #f8fafc;
    }}
    .code-block {{
        background: #0f172a;
        color: #f1f5f9;
        font-family: 'Consolas', 'Courier New', monospace;
        font-size: 8.5pt;
        padding: 10px 12px;
        border-radius: 4px;
        margin: 10px 0;
        white-space: pre;
        line-height: 1.35;
    }}
    .screenshot-block {{
        margin: 16px 0;
        page-break-inside: avoid;
        border: 1px solid #cbd5e1;
        border-radius: 6px;
        padding: 10px;
        background: #ffffff;
    }}
    .screenshot-caption {{
        font-size: 9.5pt;
        font-weight: 600;
        color: #0f172a;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        gap: 8px;
    }}
    .badge-tag {{
        background: #2563eb;
        color: #ffffff;
        font-size: 8.5pt;
        padding: 2px 7px;
        border-radius: 3px;
        font-weight: 600;
    }}
    .screenshot-img {{
        width: 100%;
        max-height: 360px;
        object-fit: contain;
        border: 1px solid #e2e8f0;
        border-radius: 4px;
        display: block;
    }}
    .page-break {{
        page-break-before: always;
    }}
</style>
</head>
<body>

<div class="header-box">
    <div class="exp-title">Experiment No. 9</div>
    <div class="exp-subtitle">Title: Design an architecture that automatically scales up and down based on traffic, with decoupled components (Database, Web App, etc.), using a Load Balancer</div>
    <table class="meta-table">
        <tr>
            <td><strong>Platform:</strong> Amazon Web Services (AWS)</td>
            <td><strong>Region:</strong> Asia Pacific (Mumbai) ap-south-1</td>
            <td><strong>Duration:</strong> 2 Hours</td>
        </tr>
        <tr>
            <td><strong>AWS Account ID:</strong> 275839157944</td>
            <td><strong>IAM User:</strong> secops-admin (Ketan_27)</td>
            <td><strong>Date of Execution:</strong> 26-Oct-2026</td>
        </tr>
    </table>
</div>

<h2>Aim</h2>
<p>To design and deploy a highly available, elastic, three-tier architecture on AWS in which the web tier (EC2 instances in an Auto Scaling Group behind an Application Load Balancer) is decoupled from the data tier (Amazon RDS MySQL), and capacity grows or shrinks automatically with traffic.</p>

<h2>Learning Objectives</h2>
<p>After completing this experiment, the student will be able to:</p>
<ol>
    <li>Explain the benefits of a decoupled, multi-tier architecture.</li>
    <li>Use the default VPC subnets in two Availability Zones and chain security groups between tiers.</li>
    <li>Configure an Application Load Balancer (ALB) with a Target Group and health checks.</li>
    <li>Create a Launch Template and an Auto Scaling Group (ASG) with a target tracking scaling policy.</li>
    <li>Deploy a managed database (Amazon RDS) in private subnets and connect the web tier to it.</li>
    <li>Generate load, observe scale-out and scale-in, and verify using CloudWatch.</li>
</ol>

<h2>Requirements</h2>
<table class="data-table">
    <thead>
        <tr><th style="width:25%;">Item</th><th>Details</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>AWS account</strong></td><td>Free Tier account (Account ID: 275839157944)</td></tr>
        <tr><td><strong>Region</strong></td><td>Asia Pacific (Mumbai) ap-south-1</td></tr>
        <tr><td><strong>Browser</strong></td><td>Chrome / Firefox</td></tr>
        <tr><td><strong>Services used</strong></td><td>VPC, EC2, ELB (ALB), Auto Scaling, RDS (MySQL), CloudWatch, IAM</td></tr>
        <tr><td><strong>Tools</strong></td><td>AWS Management Console, Python Boto3 SDK, HTTP load generator</td></tr>
    </tbody>
</table>

<h2>Theory</h2>
<h3>1. Why Decoupling?</h3>
<p>In a monolithic design, the web server and the database run on the same machine. If traffic rises, the whole machine must be scaled, and a single failure takes down everything. In a decoupled architecture, each layer is an independent component that can be scaled, patched, secured, and replaced on its own.</p>

<table class="data-table">
    <thead>
        <tr><th>Layer</th><th>AWS Service</th><th>Role</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Presentation / entry</strong></td><td>Application Load Balancer</td><td>Receives user traffic and distributes it across healthy instances</td></tr>
        <tr><td><strong>Application</strong></td><td>EC2 + Auto Scaling Group</td><td>Runs the web app; adds or removes instances automatically</td></tr>
        <tr><td><strong>Data</strong></td><td>Amazon RDS (MySQL)</td><td>Managed database, not publicly accessible, independent of web servers</td></tr>
        <tr><td><strong>Monitoring</strong></td><td>Amazon CloudWatch</td><td>Collects metrics (CPU, request count) that trigger scaling</td></tr>
    </tbody>
</table>

<h3>2. Elastic Load Balancing (ALB)</h3>
<p>An Application Load Balancer works at Layer 7 (HTTP/HTTPS). It routes requests to a Target Group, performs continuous health checks, and stops sending traffic to unhealthy instances. Because it spans multiple Availability Zones, it provides high availability.</p>

<h3>3. Auto Scaling Group (ASG)</h3>
<p>An ASG maintains a fleet of EC2 instances defined by a Launch Template (AMI, instance type, security group, user data). It specifies Minimum capacity (2), Desired capacity (2 to 4), and Maximum capacity (4). A Target Tracking Scaling Policy (target 50% CPU) automatically triggers scale-out when load rises and scale-in when load drops.</p>

<h3>4. Stateless Web Tier</h3>
<p>For scaling to work, web instances must be stateless: no persistent data is stored on the instance disk. All transactional and visit data is stored in Amazon RDS MySQL, allowing instances to be terminated freely without data loss.</p>

<div class="page-break"></div>

<h2>Architecture Diagram</h2>
<div class="code-block">
                                  Internet
                                     │
                             [ Internet Gateway ]
                                     │
                     +───────────────┴───────────────+
                     │ Application Load Balancer(ALB)│  alb-sg: HTTP 80 from anywhere (0.0.0.0/0)
                     +───────────────┬───────────────+
                                     │
                     +───────────────┴───────────────+
                     │       lab9-tg (Target Group)  │  Port 80, Health Check: /health.html
                     +───────────────┬───────────────+
                                     │
                     +───────────────+───────────────+
                     │                               │
             +───────┴───────+               +───────┴───────+
             │   EC2 (Web)   │               │   EC2 (Web)   │  Auto Scaling Group (2 to 4 instances)
             │     AZ-b      │               │     AZ-c      │  web-sg: HTTP 80 from alb-sg ONLY
             +───────┬───────+               +───────┬───────+
                     \                               /
                      \                             /
                       +─────────────┬─────────────+
                                     │
                         [ Amazon RDS MySQL (labdb) ]   db-sg: MySQL 3306 from web-sg ONLY
                         (Not publicly accessible)      Endpoint: lab9-db.cp4ig26sufqo.ap-south-1.rds.amazonaws.com

                     CloudWatch Alarm (Average CPU > 50%) ───> ASG Scales Out (2 -> 4) / Scales In (4 -> 2)
</div>

<h2>Procedure & Implementation Parameters</h2>
<table class="data-table">
    <thead>
        <tr><th>Step</th><th>Component</th><th>Configuration / Parameters Configured</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Step 1</strong></td>
            <td>Security Groups</td>
            <td>
                • <code>alb-sg</code> (sg-0bc6a4791f9aa666d): Inbound HTTP 80 from <code>0.0.0.0/0</code>.<br>
                • <code>web-sg</code> (sg-0ca9e9282a2e5acb6): Inbound HTTP 80 from <code>alb-sg</code>.<br>
                • <code>db-sg</code> (sg-04ae322910a196505): Inbound MySQL 3306 from <code>web-sg</code>.
            </td>
        </tr>
        <tr>
            <td><strong>Step 2</strong></td>
            <td>Amazon RDS</td>
            <td>Identifier: <code>lab9-db</code>, Engine: MySQL 8.0, Class: <code>db.t3.micro</code> (Free tier), Storage: 20 GiB gp2, DB: <code>labdb</code>, Automated backups: Off.</td>
        </tr>
        <tr>
            <td><strong>Step 3</strong></td>
            <td>Launch Template</td>
            <td>Template: <code>lab9-web-template</code>, AMI: Amazon Linux 2023, Type: <code>t3.micro</code>, SG: <code>web-sg</code>, Detailed CloudWatch monitoring enabled. User Data installs Apache + PHP + mysqli and connects to RDS.</td>
        </tr>
        <tr>
            <td><strong>Step 4</strong></td>
            <td>Target Group</td>
            <td>Name: <code>lab9-tg</code>, Target type: Instances, HTTP:80, Health check: <code>/health.html</code>, Healthy threshold: 2, Interval: 10s.</td>
        </tr>
        <tr>
            <td><strong>Step 5</strong></td>
            <td>Application Load Balancer</td>
            <td>Name: <code>lab9-alb</code>, Scheme: Internet-facing, Subnets: ap-south-1a, ap-south-1b, ap-south-1c, SG: <code>alb-sg</code>, Listener: HTTP 80 forward to <code>lab9-tg</code>.</td>
        </tr>
        <tr>
            <td><strong>Step 6</strong></td>
            <td>Auto Scaling Group</td>
            <td>Name: <code>lab9-asg</code>, Desired: 2, Min: 2, Max: 4. Target Tracking Policy: Average CPU Utilization 50%, Instance warmup: 60s.</td>
        </tr>
    </tbody>
</table>

<div class="page-break"></div>

<h2>Observation Table</h2>
<table class="data-table">
    <thead>
        <tr>
            <th style="width:8%;">Time</th>
            <th style="width:25%;">Load Condition</th>
            <th style="width:14%;">Avg CPU (%)</th>
            <th style="width:18%;">Desired / Running</th>
            <th>Action Taken by Auto Scaling Group</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>T0</strong></td>
            <td>No load (Baseline)</td>
            <td><strong>0.42%</strong></td>
            <td><strong>2 / 2</strong></td>
            <td>None. Baseline fleet running healthy (<code>i-05a2fbba5bad1b3f3</code>, <code>i-0189984ee89029f8d</code>).</td>
        </tr>
        <tr>
            <td><strong>T1</strong></td>
            <td>Load started (40 workers)</td>
            <td><strong>45.02%</strong></td>
            <td><strong>2 / 2</strong></td>
            <td>Concurrent HTTP requests sent to <code>/load.php</code>. CPU utilization rises sharply.</td>
        </tr>
        <tr>
            <td><strong>T2</strong></td>
            <td>Load sustained (>50%)</td>
            <td><strong>99.37%</strong></td>
            <td><strong>2 / 2 ➔ 4 / 4</strong></td>
            <td><strong>Scale-Out:</strong> CloudWatch <code>AlarmHigh</code> triggered. ASG launched 2 new instances (<code>i-0d58d8e9f305cee8a</code> and <code>i-032292c32b9f6e7d9</code>).</td>
        </tr>
        <tr>
            <td><strong>T3</strong></td>
            <td>Peak load (4 instances)</td>
            <td><strong>97.19%</strong></td>
            <td><strong>4 / 4</strong></td>
            <td>All 4 targets registered and healthy in Target Group. Traffic distributed evenly across 4 instances.</td>
        </tr>
        <tr>
            <td><strong>T4</strong></td>
            <td>Load stopped</td>
            <td><strong>14.80%</strong></td>
            <td><strong>4 / 4</strong></td>
            <td>HTTP workers terminated. CPU drops below 45% threshold. CloudWatch <code>AlarmLow</code> evaluates cool-down.</td>
        </tr>
        <tr>
            <td><strong>T5</strong></td>
            <td>After cool-down (Scale-in)</td>
            <td><strong>0.40%</strong></td>
            <td><strong>4 / 4 ➔ 2 / 2</strong></td>
            <td><strong>Scale-In:</strong> ASG terminates the 2 surplus instances to return fleet to desired capacity 2.</td>
        </tr>
    </tbody>
</table>

<h2>Attached Screenshots &amp; Verification Evidence</h2>

<div class="screenshot-block">
    <div class="screenshot-caption"><span class="badge-tag">Screenshot 1</span> Target Group with Two Healthy Targets (Step 6)</div>
    <p>Target Group <code>lab9-tg</code> in the EC2 Console showing two targets (<code>i-05a2fbba5bad1b3f3</code> in ap-south-1b and <code>i-0189984ee89029f8d</code> in ap-south-1c) passing health checks on <code>/health.html</code> with HTTP 200.</p>
    <img class="screenshot-img" src="{ss1_b64}" alt="Screenshot 1">
</div>

<div class="page-break"></div>

<div class="screenshot-block">
    <div class="screenshot-caption"><span class="badge-tag">Screenshot 2</span> ALB Web Page Showing Load Balancing &amp; Decoupled Database Visit Counter (Step 7)</div>
    <p>Verified live at <code>http://lab9-alb-1124916963.ap-south-1.elb.amazonaws.com</code>. Requests alternate between instances, and the visit counter stored in Amazon RDS MySQL increments on each request.</p>
    <img class="screenshot-img" src="{ss2_b64}" alt="Screenshot 2">
</div>

<div class="screenshot-block">
    <div class="screenshot-caption"><span class="badge-tag">Screenshot 3</span> CloudWatch AlarmHigh in the "In alarm" State Under Load (Step 8)</div>
    <p>CloudWatch Alarm <code>TargetTracking-lab9-asg-AlarmHigh</code> entering the <strong>In alarm</strong> state when average CPU utilization crossed the 50.0% threshold (evaluated at 99.37%, 97.09%, 97.19%).</p>
    <img class="screenshot-img" src="{ss3_b64}" alt="Screenshot 3">
</div>

<div class="page-break"></div>

<div class="screenshot-block">
    <div class="screenshot-caption"><span class="badge-tag">Screenshot 4</span> Auto Scaling Activity History Showing Scale-Out Launches (Step 8)</div>
    <p>EC2 Auto Scaling Groups ➔ <code>lab9-asg</code> ➔ Activity tab showing successful execution of scaling policy: desired capacity changed from 2 to 4, launching instances <code>i-0d58d8e9f305cee8a</code> and <code>i-032292c32b9f6e7d9</code>.</p>
    <img class="screenshot-img" src="{ss4_b64}" alt="Screenshot 4">
</div>

<div class="screenshot-block">
    <div class="screenshot-caption"><span class="badge-tag">Screenshot 5</span> Target Group Showing All 4 Healthy Targets Under Peak Load (Step 8)</div>
    <p>Target Group <code>lab9-tg</code> showing all 4 instances in the <strong>Healthy</strong> state, actively handling distributed user traffic across multiple availability zones.</p>
    <img class="screenshot-img" src="{ss5_b64}" alt="Screenshot 5">
</div>

<div class="page-break"></div>

<div class="screenshot-block">
    <div class="screenshot-caption"><span class="badge-tag">Screenshot 6</span> Auto Scaling Activity History Showing Scale-In / Terminating Instances (Step 9)</div>
    <p>Activity history showing low-CPU scale-in action: desired capacity reduced from 4 to 2, successfully terminating surplus instances <code>i-0d58d8e9f305cee8a</code> and <code>i-032292c32b9f6e7d9</code>.</p>
    <img class="screenshot-img" src="{ss6_b64}" alt="Screenshot 6">
</div>

<h2>Resilience Test (Fault Tolerance Verification)</h2>
<ol>
    <li><strong>Procedure:</strong> One web EC2 instance was manually terminated in the EC2 console during normal operation.</li>
    <li><strong>Observation:</strong> The Application Load Balancer health check detected the failure within 10 seconds and instantly diverted user traffic to the surviving healthy instance. The Auto Scaling Group noticed that running instances (1) fell below desired capacity (2) and automatically launched a replacement instance.</li>
    <li><strong>Outcome:</strong> The website experienced zero user downtime, demonstrating high availability and automated self-healing.</li>
</ol>

<h2>Result</h2>
<p>A decoupled, three-tier architecture was designed and implemented on AWS. The Application Load Balancer distributed traffic across EC2 instances in multiple Availability Zones, the Auto Scaling Group automatically scaled out under high CPU load and scaled in when the load decreased, and the RDS database operated independently behind its own security group, shared by all web instances.</p>

<h2>Conclusion</h2>
<p>Through this experiment, the student learned how combining an Application Load Balancer, Auto Scaling Group, and a managed RDS database yields an architecture that is scalable, highly available, fault tolerant, and cost-efficient, since capacity follows demand and each layer can evolve independently.</p>

<h2>Clean-up (Important to Avoid Charges)</h2>
<p>To ensure 100% Free Tier compliance with zero charges, resources are deleted in the following reverse order:</p>
<ol>
    <li><strong>Auto Scaling Group:</strong> <code>lab9-asg</code> (terminates all EC2 instances cleanly).</li>
    <li><strong>Load Balancer:</strong> <code>lab9-alb</code>, then Target Group <code>lab9-tg</code>.</li>
    <li><strong>Launch Template:</strong> <code>lab9-web-template</code>.</li>
    <li><strong>RDS Database:</strong> <code>lab9-db</code> (untick final snapshot and tick acknowledgement).</li>
    <li><strong>Security Groups:</strong> <code>db-sg</code>, then <code>web-sg</code>, then <code>alb-sg</code>.</li>
</ol>

</body>
</html>
"""

with open(HTML_FILE, "w", encoding="utf-8") as f:
    f.write(html)
print(f"[+] Wrote print HTML to {HTML_FILE}")

# Now call Chrome headless to compile to PDF
cmd = [
    CHROME_PATH,
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={PDF_FILE}",
    HTML_FILE
]
print("[*] Running Chrome headless to generate PDF...")
proc = subprocess.run(cmd, capture_output=True, text=True)
if os.path.exists(PDF_FILE):
    size_kb = os.path.getsize(PDF_FILE) / 1024
    print(f"[+] SUCCESS! Generated PDF: {PDF_FILE} ({size_kb:.1f} KB)")
else:
    print(f"[-] Error generating PDF. Stderr: {proc.stderr}")
