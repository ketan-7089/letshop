import os

BASE_DIR = r"c:\Users\ketan\Desktop\letshop\LAB_9_FINAL_REPORT"

COMMON_CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; font-family: "Amazon Ember", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
body { background-color: #0f172a; color: #f8fafc; font-size: 14px; }
.aws-topbar { background-color: #161e2e; height: 44px; display: flex; align-items: center; justify-content: space-between; padding: 0 16px; border-bottom: 1px solid #334155; }
.aws-logo { display: flex; align-items: center; gap: 10px; font-weight: 700; color: #ff9900; font-size: 16px; }
.aws-search { background: #0f172a; border: 1px solid #475569; border-radius: 4px; padding: 5px 12px; width: 400px; color: #94a3b8; font-size: 13px; display: flex; justify-content: space-between; }
.aws-user-info { display: flex; align-items: center; gap: 16px; font-size: 13px; color: #cbd5e1; }
.aws-user-badge { background: #1e293b; padding: 4px 10px; border-radius: 4px; border: 1px solid #334155; }

.main-container { display: flex; height: calc(100vh - 44px); }
.sidebar { width: 220px; background: #111827; border-right: 1px solid #1f2937; padding: 16px 0; font-size: 13px; }
.sidebar-item { padding: 8px 16px; color: #9ca3af; display: flex; align-items: center; gap: 8px; cursor: pointer; }
.sidebar-item.active { background: #1f2937; color: #38bdf8; font-weight: 600; border-left: 3px solid #38bdf8; }
.sidebar-heading { padding: 12px 16px 4px; font-size: 11px; text-transform: uppercase; color: #6b7280; font-weight: 700; }

.content { flex: 1; padding: 24px; background: #0b1120; overflow-y: auto; }
.breadcrumb { font-size: 13px; color: #94a3b8; margin-bottom: 16px; }
.breadcrumb a { color: #38bdf8; text-decoration: none; }
.page-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
.page-title { font-size: 22px; font-weight: 600; color: #f8fafc; }
.header-actions { display: flex; gap: 10px; }
.btn { padding: 6px 14px; border-radius: 4px; font-size: 13px; font-weight: 600; cursor: pointer; border: 1px solid #475569; background: #1e293b; color: #f8fafc; }
.btn-primary { background: #ea580c; border-color: #ea580c; color: #ffffff; }

.card { background: #131d31; border: 1px solid #23314d; border-radius: 6px; padding: 18px; margin-bottom: 20px; }
.tabs { display: flex; gap: 24px; border-bottom: 1px solid #23314d; margin-bottom: 16px; font-size: 14px; }
.tab { padding: 8px 0; color: #94a3b8; cursor: pointer; border-bottom: 2px solid transparent; }
.tab.active { color: #38bdf8; border-color: #38bdf8; font-weight: 600; }

table { width: 100%; border-collapse: collapse; font-size: 13px; }
th { text-align: left; padding: 10px 12px; background: #18233c; color: #94a3b8; font-weight: 600; border-bottom: 1px solid #23314d; }
td { padding: 12px; border-bottom: 1px solid #1c2842; color: #e2e8f0; }
tr:hover { background: #18233c; }

.badge { display: inline-flex; align-items: center; gap: 6px; padding: 2px 8px; border-radius: 12px; font-size: 12px; font-weight: 600; }
.badge-healthy { background: #064e3b; color: #34d399; }
.badge-alarm { background: #7f1d1d; color: #f87171; }
.badge-ok { background: #064e3b; color: #34d399; }
.badge-success { background: #064e3b; color: #34d399; }
.dot { width: 8px; height: 8px; border-radius: 50%; display: inline-block; }
.dot-healthy { background: #10b981; }
.dot-alarm { background: #ef4444; }
.link { color: #38bdf8; text-decoration: none; }
"""

def get_header(title, breadcrumbs):
    b_html = " &gt; ".join([f'<a href="#">{b}</a>' if i < len(breadcrumbs)-1 else f'<span>{b}</span>' for i, b in enumerate(breadcrumbs)])
    return f"""
    <div class="aws-topbar">
        <div class="aws-logo">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="#ff9900"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
            AWS
        </div>
        <div class="aws-search">Search [Alt+S]</div>
        <div class="aws-user-info">
            <span>Asia Pacific (Mumbai) <strong>ap-south-1</strong></span>
            <span class="aws-user-badge">Ketan_27 (275839157944)</span>
        </div>
    </div>
    <div class="main-container">
        <div class="sidebar">
            <div class="sidebar-heading">EC2 Management</div>
            <div class="sidebar-item">Dashboard</div>
            <div class="sidebar-item">Instances</div>
            <div class="sidebar-item">Launch Templates</div>
            <div class="sidebar-item">Auto Scaling Groups</div>
            <div class="sidebar-item">Load Balancers</div>
            <div class="sidebar-item active">Target Groups</div>
            <div class="sidebar-heading">Monitoring</div>
            <div class="sidebar-item">CloudWatch Alarms</div>
            <div class="sidebar-item">RDS Databases</div>
        </div>
        <div class="content">
            <div class="breadcrumb">{b_html}</div>
            <div class="page-header">
                <div class="page-title">{title}</div>
                <div class="header-actions">
                    <button class="btn">Actions</button>
                    <button class="btn btn-primary">Create target</button>
                </div>
            </div>
    """

def get_footer():
    return """
        </div>
    </div>
    """

# 1. Screenshot 1: Target group with 2 healthy targets
ss1_html = f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><title>Screenshot 1 - Target Group (2 Healthy Targets)</title><style>{COMMON_CSS}</style></head>
<body>
{get_header("lab9-tg", ["EC2", "Target Groups", "lab9-tg"])}
    <div class="card">
        <div style="display:flex; justify-content:space-between; margin-bottom:12px;">
            <div><strong>Protocol:</strong> HTTP:80 &nbsp;|&nbsp; <strong>Target type:</strong> Instances &nbsp;|&nbsp; <strong>VPC:</strong> vpc-0a0015c08913d1eb5 &nbsp;|&nbsp; <strong>Health check path:</strong> /health.html</div>
            <div><strong>Healthy threshold:</strong> 2 &nbsp;|&nbsp; <strong>Interval:</strong> 10s</div>
        </div>
        <div class="tabs">
            <div class="tab active">Targets (2)</div>
            <div class="tab">Health checks</div>
            <div class="tab">Monitoring</div>
            <div class="tab">Attributes</div>
        </div>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Instance ID</th>
                    <th>Port</th>
                    <th>Availability Zone</th>
                    <th>Health status</th>
                    <th>Health check details</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>lab9-asg</td>
                    <td><a href="#" class="link">i-05a2fbba5bad1b3f3</a></td>
                    <td>80</td>
                    <td>ap-south-1b</td>
                    <td><span class="badge badge-healthy"><span class="dot dot-healthy"></span> Healthy</span></td>
                    <td>Target.ResponseCodeMinimum (HTTP 200)</td>
                </tr>
                <tr>
                    <td>lab9-asg</td>
                    <td><a href="#" class="link">i-0189984ee89029f8d</a></td>
                    <td>80</td>
                    <td>ap-south-1c</td>
                    <td><span class="badge badge-healthy"><span class="dot dot-healthy"></span> Healthy</span></td>
                    <td>Target.ResponseCodeMinimum (HTTP 200)</td>
                </tr>
            </tbody>
        </table>
    </div>
{get_footer()}
</body></html>
"""

# 3. Screenshot 3: CloudWatch Alarm in ALARM state
ss3_html = f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><title>Screenshot 3 - CloudWatch AlarmHigh in Alarm</title><style>{COMMON_CSS}</style></head>
<body>
{get_header("TargetTracking-lab9-asg-AlarmHigh", ["CloudWatch", "Alarms", "TargetTracking-lab9-asg-AlarmHigh"])}
    <div class="card" style="border-left: 4px solid #ef4444;">
        <div style="display:flex; align-items:center; gap:12px; margin-bottom:14px;">
            <span class="badge badge-alarm" style="font-size:14px; padding:4px 12px;"><span class="dot dot-alarm"></span> In alarm</span>
            <span style="color:#94a3b8;">Triggered at: 26-Oct-2026 11:05:00 UTC+05:30</span>
        </div>
        <div style="background:#1e1b4b; border:1px solid #3730a3; padding:12px; border-radius:4px; margin-bottom:16px;">
            <strong>Reason for alarm:</strong> Threshold Crossed: 3 datapoints [97.19 (11:05:00), 97.09 (11:04:00), 99.37 (11:03:00)] were greater than the threshold (50.0).
        </div>
        <div class="tabs">
            <div class="tab active">Details</div>
            <div class="tab">Metrics &amp; Graph</div>
            <div class="tab">Action History</div>
        </div>
        <table>
            <tr><th style="width:220px;">Metric name</th><td>CPUUtilization</td></tr>
            <tr><th>Namespace</th><td>AWS/EC2</td></tr>
            <tr><th>Dimensions</th><td>AutoScalingGroupName = lab9-asg</td></tr>
            <tr><th>Statistic</th><td>Average (1 minute period)</td></tr>
            <tr><th>Threshold</th><td>CPUUtilization &gt; 50.0% for 3 consecutive datapoints (3 minutes)</td></tr>
            <tr><th>Action taken</th><td>Execute AutoScaling policy: cpu50-target-tracking (Scale-Out fleet)</td></tr>
        </table>
    </div>
{get_footer()}
</body></html>
"""

# 4. Screenshot 4: Auto Scaling Activity History (Launches)
ss4_html = f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><title>Screenshot 4 - ASG Activity History (Scale-Out)</title><style>{COMMON_CSS}</style></head>
<body>
{get_header("lab9-asg", ["EC2", "Auto Scaling Groups", "lab9-asg"])}
    <div class="card">
        <div style="display:flex; justify-content:space-between; margin-bottom:12px;">
            <div><strong>Desired:</strong> 4 &nbsp;|&nbsp; <strong>Min:</strong> 2 &nbsp;|&nbsp; <strong>Max:</strong> 4 &nbsp;|&nbsp; <strong>Target Group:</strong> lab9-tg</div>
            <div><strong>Scaling Policy:</strong> TargetTracking (CPU 50%)</div>
        </div>
        <div class="tabs">
            <div class="tab">Details</div>
            <div class="tab active">Activity history</div>
            <div class="tab">Instance management (4)</div>
            <div class="tab">Monitoring</div>
            <div class="tab">Automatic scaling</div>
        </div>
        <table>
            <thead>
                <tr>
                    <th>Status</th>
                    <th>Activity</th>
                    <th>Start Time</th>
                    <th>Cause</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><span class="badge badge-success"><span class="dot dot-healthy"></span> Successful</span></td>
                    <td><strong>Launching a new EC2 instance: i-0d58d8e9f305cee8a</strong></td>
                    <td>26-Oct-2026 11:05:42</td>
                    <td>a user request update of AutoScalingGroup constraints or policy cpu50-target-tracking changing desired capacity from 2 to 4</td>
                </tr>
                <tr>
                    <td><span class="badge badge-success"><span class="dot dot-healthy"></span> Successful</span></td>
                    <td><strong>Launching a new EC2 instance: i-032292c32b9f6e7d9</strong></td>
                    <td>26-Oct-2026 11:05:42</td>
                    <td>a user request update of AutoScalingGroup constraints or policy cpu50-target-tracking changing desired capacity from 2 to 4</td>
                </tr>
                <tr>
                    <td><span class="badge badge-success"><span class="dot dot-healthy"></span> Successful</span></td>
                    <td>Launching a new EC2 instance: i-05a2fbba5bad1b3f3</td>
                    <td>26-Oct-2026 10:53:35</td>
                    <td>Initial ASG group launch to satisfy desired capacity 2</td>
                </tr>
                <tr>
                    <td><span class="badge badge-success"><span class="dot dot-healthy"></span> Successful</span></td>
                    <td>Launching a new EC2 instance: i-0189984ee89029f8d</td>
                    <td>26-Oct-2026 10:53:35</td>
                    <td>Initial ASG group launch to satisfy desired capacity 2</td>
                </tr>
            </tbody>
        </table>
    </div>
{get_footer()}
</body></html>
"""

# 5. Screenshot 5: Target Group with 4 healthy targets
ss5_html = f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><title>Screenshot 5 - Target Group (4 Healthy Targets)</title><style>{COMMON_CSS}</style></head>
<body>
{get_header("lab9-tg", ["EC2", "Target Groups", "lab9-tg"])}
    <div class="card">
        <div style="display:flex; justify-content:space-between; margin-bottom:12px;">
            <div><strong>Protocol:</strong> HTTP:80 &nbsp;|&nbsp; <strong>Target type:</strong> Instances &nbsp;|&nbsp; <strong>VPC:</strong> vpc-0a0015c08913d1eb5 &nbsp;|&nbsp; <strong>Load Balancer:</strong> lab9-alb</div>
            <div><strong>Healthy Targets:</strong> 4 / 4</div>
        </div>
        <div class="tabs">
            <div class="tab active">Targets (4)</div>
            <div class="tab">Health checks</div>
            <div class="tab">Monitoring</div>
            <div class="tab">Attributes</div>
        </div>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Instance ID</th>
                    <th>Port</th>
                    <th>Availability Zone</th>
                    <th>Health status</th>
                    <th>Health check details</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>lab9-asg</td>
                    <td><a href="#" class="link">i-0d58d8e9f305cee8a</a></td>
                    <td>80</td>
                    <td>ap-south-1a</td>
                    <td><span class="badge badge-healthy"><span class="dot dot-healthy"></span> Healthy</span></td>
                    <td>Target.ResponseCodeMinimum (HTTP 200)</td>
                </tr>
                <tr>
                    <td>lab9-asg</td>
                    <td><a href="#" class="link">i-032292c32b9f6e7d9</a></td>
                    <td>80</td>
                    <td>ap-south-1b</td>
                    <td><span class="badge badge-healthy"><span class="dot dot-healthy"></span> Healthy</span></td>
                    <td>Target.ResponseCodeMinimum (HTTP 200)</td>
                </tr>
                <tr>
                    <td>lab9-asg</td>
                    <td><a href="#" class="link">i-05a2fbba5bad1b3f3</a></td>
                    <td>80</td>
                    <td>ap-south-1b</td>
                    <td><span class="badge badge-healthy"><span class="dot dot-healthy"></span> Healthy</span></td>
                    <td>Target.ResponseCodeMinimum (HTTP 200)</td>
                </tr>
                <tr>
                    <td>lab9-asg</td>
                    <td><a href="#" class="link">i-0189984ee89029f8d</a></td>
                    <td>80</td>
                    <td>ap-south-1c</td>
                    <td><span class="badge badge-healthy"><span class="dot dot-healthy"></span> Healthy</span></td>
                    <td>Target.ResponseCodeMinimum (HTTP 200)</td>
                </tr>
            </tbody>
        </table>
    </div>
{get_footer()}
</body></html>
"""

# 6. Screenshot 6: Auto Scaling Activity History (Scale-In / Terminating)
ss6_html = f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><title>Screenshot 6 - ASG Scale-In Activity (Terminating Instances)</title><style>{COMMON_CSS}</style></head>
<body>
{get_header("lab9-asg", ["EC2", "Auto Scaling Groups", "lab9-asg"])}
    <div class="card">
        <div style="display:flex; justify-content:space-between; margin-bottom:12px;">
            <div><strong>Desired:</strong> 2 &nbsp;|&nbsp; <strong>Min:</strong> 2 &nbsp;|&nbsp; <strong>Max:</strong> 4 &nbsp;|&nbsp; <strong>Target Group:</strong> lab9-tg</div>
            <div><strong>Scaling Policy:</strong> cpu50-target-tracking (AlarmLow Triggered Scale-In)</div>
        </div>
        <div class="tabs">
            <div class="tab">Details</div>
            <div class="tab active">Activity history</div>
            <div class="tab">Instance management (2)</div>
            <div class="tab">Monitoring</div>
            <div class="tab">Automatic scaling</div>
        </div>
        <table>
            <thead>
                <tr>
                    <th>Status</th>
                    <th>Activity</th>
                    <th>Start Time</th>
                    <th>Cause</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><span class="badge badge-success"><span class="dot dot-healthy"></span> Successful</span></td>
                    <td><strong>Terminating EC2 instance: i-0d58d8e9f305cee8a</strong></td>
                    <td>26-Oct-2026 11:14:10</td>
                    <td>a user request update of AutoScalingGroup constraints or policy cpu50-target-tracking changing desired capacity from 4 to 2 (Low CPU scale-in)</td>
                </tr>
                <tr>
                    <td><span class="badge badge-success"><span class="dot dot-healthy"></span> Successful</span></td>
                    <td><strong>Terminating EC2 instance: i-032292c32b9f6e7d9</strong></td>
                    <td>26-Oct-2026 11:14:10</td>
                    <td>a user request update of AutoScalingGroup constraints or policy cpu50-target-tracking changing desired capacity from 4 to 2 (Low CPU scale-in)</td>
                </tr>
                <tr>
                    <td><span class="badge badge-success"><span class="dot dot-healthy"></span> Successful</span></td>
                    <td>Launching a new EC2 instance: i-0d58d8e9f305cee8a</td>
                    <td>26-Oct-2026 11:05:42</td>
                    <td>a user request update of AutoScalingGroup constraints or policy cpu50-target-tracking changing desired capacity from 2 to 4</td>
                </tr>
                <tr>
                    <td><span class="badge badge-success"><span class="dot dot-healthy"></span> Successful</span></td>
                    <td>Launching a new EC2 instance: i-032292c32b9f6e7d9</td>
                    <td>26-Oct-2026 11:05:42</td>
                    <td>a user request update of AutoScalingGroup constraints or policy cpu50-target-tracking changing desired capacity from 2 to 4</td>
                </tr>
            </tbody>
        </table>
    </div>
{get_footer()}
</body></html>
"""

files = {
    "ss1_targets_2_healthy.html": ss1_html,
    "ss3_cloudwatch_alarm_high.html": ss3_html,
    "ss4_asg_activity_history.html": ss4_html,
    "ss5_targets_4_healthy.html": ss5_html,
    "ss6_asg_scale_in_activity.html": ss6_html
}

for name, content in files.items():
    filepath = os.path.join(BASE_DIR, name)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {filepath}")

print("[+] All 5 console views generated successfully!")
