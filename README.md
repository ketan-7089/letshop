# LetShop - E-Commerce Web Application & CI/CD Pipeline

LetShop is a modern, responsive e-commerce Single Page Application (SPA) built with React, TypeScript, and Vite. This repository includes an automated Continuous Integration and Continuous Deployment (CI/CD) pipeline using **Jenkins** and **AWS EC2 (Ubuntu + Nginx)**.

---

## 1. Technologies Used

- **Frontend**: React 18, TypeScript, Vite 5
- **UI & Styling**: Tailwind CSS, Radix UI Primitives, Lucide Icons, TanStack Query
- **Testing**: Vitest, React Testing Library, jsdom, Jest-DOM
- **CI/CD Automation**: Jenkins Declarative Pipeline (`Jenkinsfile`)
- **Deployment Platform**: AWS EC2 Linux Instance (Ubuntu / Amazon Linux)
- **Web Server**: Nginx (reverse proxy & static SPA file server)

---

## 2. Local Development & Setup

### Prerequisites
- Node.js (v18 or higher recommended, e.g., v20/v22)
- npm (v9 or higher)

### Installation
Clone the repository and install dependencies using `npm ci`:
```bash
git clone <YOUR_GIT_REPOSITORY_URL>
cd letshop
npm ci
```

### Running Locally
Start the local Vite development server:
```bash
npm run dev
```
Open your browser at `http://localhost:5173`.

---

## 3. Automated Testing, Building, and Quality

### Run Unit Tests
Execute the unit test suite non-interactively using Vitest:
```bash
npm test
```
The test suite runs offline and verifies core component rendering (e.g., brand title, navigation routes, and theme toggling in `src/components/Header.tsx`).

### Production Build
Generate optimized static production assets in the `dist/` directory:
```bash
npm run build
```

### Linting
Validate TypeScript and React code conventions:
```bash
npm run lint
```

---

## 4. CI/CD Architecture & Workflow

The pipeline implements an automated DevOps workflow:

```
[ Developer Push ] ──> [ GitHub Repository ]
                              │
                              ▼ (Webhook / SCM Polling)
                       [ Jenkins Agent ]
                              │
                              ├── 1. Checkout (Git clone)
                              ├── 2. Install Dependencies (npm ci)
                              ├── 3. Test (npm test via Vitest)
                              ├── 4. Build (npm run build -> dist/)
                              ├── 5. Deploy (Package tarball -> scp to EC2 -> deploy.sh)
                              └── 6. Verify (HTTP health check via curl)
                                      │
                                      ▼
                             [ AWS EC2 Instance ]
                                      │
                                      ▼
                             [ Nginx Web Server ]
                                      │
                                      ▼
                             [ User Browser : Port 80 ]
```

---

## 5. AWS EC2 Server One-Time Setup

Before triggering the first automated deployment from Jenkins, complete the initial setup on your AWS EC2 instance.

### A. AWS Security Group Configuration
In the AWS Management Console, ensure your EC2 Security Group allows the following inbound ports:
- **Port 22 (SSH)**: From your Jenkins Server IP (or `0.0.0.0/0` for practical testing).
- **Port 80 (HTTP)**: From `0.0.0.0/0` (allows public web access to LetShop).

### B. Connect to your EC2 Instance
```bash
ssh -i /path/to/your-key.pem ubuntu@<EC2_PUBLIC_IP>
```

### C. Install Nginx
```bash
sudo apt update
sudo apt install -y nginx
sudo systemctl enable nginx
sudo systemctl start nginx
```

### D. Configure Nginx for LetShop
1. Copy the provided [`nginx.conf`](./nginx.conf) to Nginx's sites configuration:
```bash
sudo nano /etc/nginx/sites-available/letshop
```
*(Paste the contents of [`nginx.conf`](./nginx.conf) from this repository into that file).*

2. Enable the LetShop site and disable the default Nginx welcome page:
```bash
sudo ln -sf /etc/nginx/sites-available/letshop /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default
```

3. Test and reload Nginx:
```bash
sudo nginx -t
sudo systemctl reload nginx
```

### E. Prepare the Web Root Directory
Create the target web root directory and assign ownership to the web server user:
```bash
sudo mkdir -p /var/www/letshop
sudo chown -R www-data:www-data /var/www/letshop
sudo chmod -R 755 /var/www/letshop
```

### F. Allow Non-Interactive Reload for Deployment (Optional for Jenkins)
To allow the deployment script to reload Nginx without prompting for a password:
```bash
sudo visudo
```
Add this line at the bottom:
```
ubuntu ALL=(ALL) NOPASSWD: /bin/systemctl reload nginx, /usr/bin/systemctl reload nginx, /bin/mkdir, /bin/tar, /bin/chown, /bin/chmod, /bin/rm
```

---

## 6. Jenkins Pipeline Configuration

### A. Required Jenkins Plugins
Ensure the following plugins are installed in Jenkins (**Manage Jenkins** → **Plugins**):
- **Git Plugin** (for checking out source code)
- **Pipeline Plugin** (for executing `Jenkinsfile`)
- **SSH Agent Plugin** (for SSH credentials handling)

### B. Add EC2 SSH Credentials to Jenkins
1. Go to **Manage Jenkins** → **Credentials** → **System** → **Global credentials** → **Add Credentials**.
2. Select **Kind**: `SSH Username with private key`.
3. **ID**: `ec2-ssh-key` *(or matches the value provided in the pipeline parameter)*.
4. **Username**: `ubuntu` (or `ec2-user` depending on your EC2 Linux AMI).
5. **Private Key**: Select **Enter directly** and paste the contents of your `.pem` private key file.
6. Click **Create**.

### C. Create the Pipeline Job
1. In Jenkins dashboard, click **New Item** → Enter name (e.g. `LetShop-Pipeline`) → Select **Pipeline** → Click **OK**.
2. Scroll to the **Pipeline** section:
   - **Definition**: Select `Pipeline script from SCM`.
   - **SCM**: Select `Git`.
   - **Repository URL**: Your GitHub repository URL.
   - **Branch Specifier**: `*/main`.
   - **Script Path**: `Jenkinsfile`.
3. Click **Save**.

### D. Running the Pipeline
Click **Build with Parameters**:
- `EC2_HOST`: Enter the Public IP or DNS of your AWS EC2 instance (e.g., `54.210.xx.xx`).
- `EC2_USER`: `ubuntu` (default).
- `SSH_CRED_ID`: `ec2-ssh-key` (default).
- `DEPLOY_DIR`: `/var/www/letshop` (default).

Click **Build**.

---

## 7. Verifying Deployment

Once Jenkins completes the deployment:
1. **Application**: Open your browser and navigate to:
   ```
   http://<EC2_PUBLIC_IP>/
   ```
   You should see the LetShop home page running live.
2. **Health Check Endpoint**:
   ```
   http://<EC2_PUBLIC_IP>/health.json
   ```
   Returns:
   ```json
   {
     "status": "ok",
     "app": "letshop",
     "version": "1.0.0"
   }
   ```
3. **SPA Client Routing**: Test visiting sub-routes such as `http://<EC2_PUBLIC_IP>/products` or `http://<EC2_PUBLIC_IP>/cart`. Nginx will properly redirect route requests to `index.html` via `try_files $uri $uri/ /index.html;`.
