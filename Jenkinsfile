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
                    // Create and activate a virtual environment
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
                    // Start Flask app (in the background) and wait for it to start
                    sh '''
                        source venv/bin/activate
                        python app.py &
                        sleep 10
                    '''
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
