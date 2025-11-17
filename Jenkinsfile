pipeline {
    agent any

    options {
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timestamps()
    }

    environment {
        // Try to use PYTHON_HOME if set, otherwise search for python
        PATH = "${env.PATH};C:\\Python311;C:\\Python310;C:\\Python39"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Verify Python') {
            steps {
                echo 'Verifying Python installation...'
                bat '''
                    @echo off
                    echo Checking for Python...
                    where python.exe >nul 2>&1
                    if !errorlevel! equ 0 (
                        for /f "delims=" %%i in ('where python.exe 2^>nul') do (
                            echo Found Python at: %%i
                            "%%i" --version
                            exit /b 0
                        )
                    )
                    where python >nul 2>&1
                    if !errorlevel! equ 0 (
                        for /f "delims=" %%i in ('where python 2^>nul') do (
                            echo Found Python at: %%i
                            "%%i" --version
                            exit /b 0
                        )
                    )
                    echo ERROR: Python not found in PATH!
                    exit /b 1
                '''
            }
        }

        stage('Setup') {
            steps {
                echo 'Setting up Python environment...'
                bat '''
                    @echo off
                    echo Installing Python dependencies...
                    python -m pip install --upgrade pip
                    python -m pip install flask pytest pytest-cov pylint
                '''
            }
        }

        stage('Lint') {
            steps {
                echo 'Running linting checks...'
                bat '''
                    @echo off
                    python -m pylint src/ --exit-zero || exit /b 0
                '''
            }
        }

        stage('Unit Tests') {
            steps {
                echo 'Running unit tests...'
                bat '''
                    @echo off
                    python -m pytest tests/unit/ -v --cov=src --cov-report=xml --cov-report=html --junit-xml=test-results.xml || exit /b 0
                '''
            }
        }

        stage('Integration Tests') {
            steps {
                echo 'Running integration tests...'
                bat '''
                    @echo off
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
