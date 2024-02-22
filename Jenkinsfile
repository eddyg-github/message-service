pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                script {
                    sh 'python -m venv venv'
                    sh 'source venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Add any testing commands if needed
                }
            }
        }

        stage('Run Flask App') {
            steps {
                script {
                    sh 'source venv/bin/activate && python app.py &'
                    // Use `sleep` to give time for the server to start
                    sleep 10
                }
            }
        }
    }

    post {
        always {
            script {
                // Clean up
                sh 'killall python || true'
                sh 'deactivate || true'
            }
        }
    }
}
