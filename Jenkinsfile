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
                sh '''
                    python --version
                    pip install --upgrade pip
                    pip install -r requirements.txt || pip install flask pytest pytest-cov
                '''
            }
        }

        stage('Lint') {
            steps {
                echo 'Running linting checks...'
                sh '''
                    pip install pylint || true
                    pylint src/ --exit-zero || true
                '''
            }
        }

        stage('Unit Tests') {
            steps {
                echo 'Running unit tests...'
                sh '''
                    pytest tests/unit/ -v --cov=src --cov-report=xml --cov-report=html
                '''
            }
        }

        stage('Integration Tests') {
            steps {
                echo 'Running integration tests...'
                sh '''
                    pytest tests/integration/ -v || true
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
            junit 'test-results.xml' || true
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
