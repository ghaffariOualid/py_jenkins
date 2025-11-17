pipeline {
    agent any


    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                bat 'python -m pip install --upgrade pip flask pytest pytest-cov pylint'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                bat 'python -m pytest tests/ -v --junit-xml=test-results.xml'
            }
        }

        stage('Code Coverage') {
            steps {
                echo 'Running coverage analysis...'
                bat 'python -m pytest tests/ --cov=src --cov-report=html --cov-report=xml'
            }
        }

       
    }

    post {
        always {
            echo 'Pipeline completed'
           
        }
        success {
            echo 'Success!'
        }
        failure {
            echo 'Failed!'
        }
    }
}
