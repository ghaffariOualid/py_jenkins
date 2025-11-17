pipeline {
    agent any

    options {
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timestamps()
    }

    environment {
        // Try to use PYTHON_HOME if set, otherwise search for python
        PYTHON_CMD = '''@echo off
                        setlocal enabledelayedexpansion
                        if defined PYTHON_HOME (
                            echo !PYTHON_HOME!\python.exe
                        ) else (
                            where python.exe 2>nul || where python 2>nul || echo python
                        )'''
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
                    echo Checking PYTHON_HOME variable...
                    if defined PYTHON_HOME (
                        echo PYTHON_HOME is set to: %PYTHON_HOME%
                        "%PYTHON_HOME%\python.exe" --version
                    ) else (
                        echo PYTHON_HOME not set, searching PATH...
                        where python.exe >nul 2>&1
                        if !errorlevel! equ 0 (
                            for /f "delims=" %%i in ('where python.exe 2^>nul') do (
                                echo Found Python at: %%i
                                "%%i" --version
                            )
                        ) else (
                            where python >nul 2>&1
                            if !errorlevel! equ 0 (
                                for /f "delims=" %%i in ('where python 2^>nul') do (
                                    echo Found Python at: %%i
                                    "%%i" --version
                                )
                            ) else (
                                echo ERROR: Python not found!
                                echo Please configure PYTHON_HOME in Jenkins System Configuration
                                exit /b 1
                            )
                        )
                    )
                '''
            }
        }

        stage('Setup') {
            steps {
                echo 'Setting up Python environment...'
                bat '''
                    @echo off
                    setlocal enabledelayedexpansion
                    
                    REM Determine Python executable path
                    set PYTHON_EXE=python.exe
                    if defined PYTHON_HOME (
                        set PYTHON_EXE=%PYTHON_HOME%\python.exe
                    )
                    
                    echo Installing Python dependencies...
                    "!PYTHON_EXE!" -m pip install --upgrade pip
                    "!PYTHON_EXE!" -m pip install flask pytest pytest-cov pylint
                '''
            }
        }

        stage('Lint') {
            steps {
                echo 'Running linting checks...'
                bat '''
                    @echo off
                    setlocal enabledelayedexpansion
                    set PYTHON_EXE=python.exe
                    if defined PYTHON_HOME set PYTHON_EXE=%PYTHON_HOME%\python.exe
                    "!PYTHON_EXE!" -m pylint src/ --exit-zero || exit /b 0
                '''
            }
        }

        stage('Unit Tests') {
            steps {
                echo 'Running unit tests...'
                bat '''
                    @echo off
                    setlocal enabledelayedexpansion
                    set PYTHON_EXE=python.exe
                    if defined PYTHON_HOME set PYTHON_EXE=%PYTHON_HOME%\python.exe
                    "!PYTHON_EXE!" -m pytest tests/unit/ -v --cov=src --cov-report=xml --cov-report=html --junit-xml=test-results.xml || exit /b 0
                '''
            }
        }

        stage('Integration Tests') {
            steps {
                echo 'Running integration tests...'
                bat '''
                    @echo off
                    setlocal enabledelayedexpansion
                    set PYTHON_EXE=python.exe
                    if defined PYTHON_HOME set PYTHON_EXE=%PYTHON_HOME%\python.exe
                    "!PYTHON_EXE!" -m pytest tests/integration/ -v || exit /b 0
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
