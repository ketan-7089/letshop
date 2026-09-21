pipeline {
    agent any

    parameters {
        string(name: 'EC2_HOST', defaultValue: '', description: 'AWS EC2 Public IP or DNS address')
        string(name: 'EC2_USER', defaultValue: 'ubuntu', description: 'SSH username for EC2 (e.g., ubuntu or ec2-user)')
        string(name: 'SSH_CRED_ID', defaultValue: 'ec2-ssh-key', description: 'Jenkins credential ID for EC2 SSH Private Key')
        string(name: 'DEPLOY_DIR', defaultValue: '/var/www/letshop', description: 'Target directory on EC2 server')
    }

    environment {
        CI = 'true'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code from Git...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies cleanly using npm ci...'
                sh 'npm ci'
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated tests with Vitest...'
                sh 'npm test'
            }
        }

        stage('Build') {
            steps {
                echo 'Building production Vite bundle...'
                sh 'npm run build'
            }
        }

        stage('Deploy') {
            steps {
                script {
                    def ec2Host = params.EC2_HOST?.trim() ?: env.EC2_HOST?.trim()
                    def ec2User = params.EC2_USER?.trim() ?: (env.EC2_USER?.trim() ?: 'ubuntu')
                    def sshCred = params.SSH_CRED_ID?.trim() ?: (env.SSH_CRED_ID?.trim() ?: 'ec2-ssh-key')
                    def deployDir = params.DEPLOY_DIR?.trim() ?: '/var/www/letshop'

                    if (!ec2Host) {
                        echo "================================================================="
                        echo "SKIPPING DEPLOYMENT: EC2_HOST parameter is not configured."
                        echo "Provide EC2_HOST (e.g. 54.x.x.x) when triggering the build to deploy."
                        echo "================================================================="
                        return
                    }

                    echo "Packaging production build to dist.tar.gz..."
                    sh 'tar -czf dist.tar.gz -C dist .'

                    echo "Transferring build to AWS EC2 (${ec2User}@${ec2Host})..."
                    sshagent([sshCred]) {
                        sh """
                            # Copy archive and deployment script to EC2 /tmp directory using scp
                            scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null dist.tar.gz deploy.sh ${ec2User}@${ec2Host}:/tmp/

                            # Execute deployment script on EC2 host
                            ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null ${ec2User}@${ec2Host} "chmod +x /tmp/deploy.sh && /tmp/deploy.sh /tmp/dist.tar.gz ${deployDir}"
                        """
                    }
                }
            }
        }

        stage('Verify') {
            steps {
                script {
                    def ec2Host = params.EC2_HOST?.trim() ?: env.EC2_HOST?.trim()

                    if (!ec2Host) {
                        echo "SKIPPING VERIFICATION: EC2_HOST is not configured."
                        return
                    }

                    echo "Running health check against http://${ec2Host}/health.json..."
                    sh """
                        # Verify health endpoint returns HTTP 200 OK
                        curl -f -s -S --retry 3 --retry-delay 5 http://${ec2Host}/health.json
                        echo ""
                        echo "Checking HTTP root response:"
                        curl -s -I http://${ec2Host}/ | head -n 5
                    """
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline run completed for build #${env.BUILD_NUMBER}."
            // Clean up temporary local archive
            sh 'rm -f dist.tar.gz'
        }
        success {
            echo "Build, test, and deployment completed successfully!"
        }
        failure {
            echo "Pipeline failed! Please inspect the console log above for details."
        }
    }
}
