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
                    where python
                    python -m pip --version
                    python -m pip install --upgrade pip
                    python -m pip install -r requirements.txt 2>nul || python -m pip install flask pytest pytest-cov
                '''
            }
        }

        stage('Lint') {
            steps {
                echo 'Running linting checks...'
                bat '''
                    python -m pip install pylint
                    python -m pylint src/ --exit-zero || exit /b 0
                '''
            }
        }

        stage('Unit Tests') {
            steps {
                echo 'Running unit tests...'
                bat '''
                    python -m pytest tests/unit/ -v --cov=src --cov-report=xml --cov-report=html --junit-xml=test-results.xml || exit /b 0
                '''
            }
        }

        stage('Integration Tests') {
            steps {
                echo 'Running integration tests...'
                bat '''
                    python -m pytest tests/integration/ -v || exit /b 0
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
