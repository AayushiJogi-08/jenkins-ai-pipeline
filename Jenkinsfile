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
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Build Model') {
            steps {
                bat 'python main.py'
            }
        }

        stage('Test Model') {
            steps {
                bat 'python -m unittest test_main.py'
            }
        }
    }

    post {
        success {
            archiveArtifacts artifacts: 'model.pkl', fingerprint: true
        }
    }
}