pipeline {
    agent any
    stages {
        stage('1. Pull Source Code') {
            steps {
                // Pull latest source code from Git repository, Jenkins auto config without manual git commands
                checkout scm
            }
        }
        stage('2. CI Build Image') {
            steps {
                sh '''
                docker rm -f flask-web || true
                docker rmi -f flask-app:latest || true
                docker build -t flask-app:latest .
                '''
            }
        }
        stage('3. CD Deploy Restart Service') {
            steps {
                sh '''
                docker run -d --name flask-web -p 5000:5000 flask-app:latest
                '''
            }
        }
    }
    post {
        success {
            echo "Auto deployment finished, visit http://localhost:5000 to check new version"
        }
    }
}