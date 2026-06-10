pipeline {
    agent any

    environment {
        PYTHON = "C:\\Users\\GANESH\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe"
        PIP = "C:\\Users\\GANESH\\AppData\\Local\\Python\\pythoncore-3.14-64\\Scripts\\pip.exe"
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Cloning repository from GitHub...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                bat '"%PIP%" install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running unit tests...'
                bat '"%PYTHON%" -m pytest tests/ -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                bat 'docker build -t flask-cicd-app:latest .'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                echo 'Deployment stage ready for Kubernetes integration.'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}