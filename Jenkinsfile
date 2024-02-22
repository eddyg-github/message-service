pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Paso para checkout del repositorio
                checkout scm
            }
        }

        stage('Build') {
            steps {
                // Aquí coloca los pasos para compilar tu proyecto
                script {
                    // Por ejemplo:
                    sh 'mvn clean install'
                }
            }
        }

        stage('Test') {
            steps {
                // Aquí coloca los pasos para ejecutar pruebas
                script {
                    // Por ejemplo:
                    sh 'mvn test'
                }
            }
        }

        stage('Deploy') {
            steps {
                // Aquí coloca los pasos para implementar tu aplicación
                script {
                    // Por ejemplo:
                    sh 'deploy-script.sh'
                }
            }
        }
    }

    post {
        success {
            // Acciones a realizar si la construcción es exitosa
            echo 'Build successful!'

            // Puedes agregar más pasos o acciones aquí
        }

        failure {
            // Acciones a realizar si la construcción falla
            echo 'Build failed!'

            // Puedes agregar más pasos o acciones aquí
        }
    }
}
