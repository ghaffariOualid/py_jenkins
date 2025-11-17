pipeline {
    agent any


    stages {
        stage('Checkout') {
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

        stage('Linting') {
            steps {
                echo 'Running linting checks...'
                bat 'python -m pylint src/ --exit-zero || exit /b 0'
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed'
            junit testResults: 'test-results.xml', allowEmptyResults: true
        }
        success {
            echo 'Success!'
        }
        failure {
            echo 'Failed!'
        }
    }
}
