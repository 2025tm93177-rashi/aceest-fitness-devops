pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build & Lint') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    flake8 app.py test_app.py
                '''
            }
        }

        stage('Run Pytest') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest test_app.py --verbose
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t aceest-fitness-app:${BUILD_NUMBER} .'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
