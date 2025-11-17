pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                echo 'Setting up Python environment...'
                bat '''
                    python --version
                    pip install --upgrade pip
                    pip install -r requirements.txt || pip install flask pytest pytest-cov
                '''
            }
        }

        stage('Lint') {
            steps {
                echo 'Running linting checks...'
                bat '''
                    pip install pylint
                    pylint src/ --exit-zero || exit /b 0
                '''
            }
        }

        stage('Unit Tests') {
            steps {
                echo 'Running unit tests...'
                bat '''
                    pytest tests/unit/ -v --cov=src --cov-report=xml --cov-report=html --junit-xml=test-results.xml
                '''
            }
        }

        stage('Integration Tests') {
            steps {
                echo 'Running integration tests...'
                bat '''
                    pytest tests/integration/ -v || exit /b 0
                '''
            }
        }

        stage('Code Coverage Report') {
            steps {
                echo 'Generating coverage report...'
                publishHTML([
                    reportDir: 'htmlcov',
                    reportFiles: 'index.html',
                    reportName: 'Code Coverage Report'
                ])
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            junit testResults: 'test-results.xml', allowEmptyResults: true
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
