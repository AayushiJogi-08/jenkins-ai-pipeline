pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Build Model') {
            steps {
                sh 'python main.py'
            }
        }

        stage('Test Model') {
            steps {
                sh 'python -m unittest test_main.py'
            }
        }
    }

    post {
        success {
            archiveArtifacts artifacts: 'model.pkl', fingerprint: true
        }
    }
}