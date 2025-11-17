@echo off
REM Script to configure Jenkins for Python builds
REM Run this on the Jenkins agent/controller machine

echo Configuring Jenkins for Python...

REM Find Python installation
for /f "delims=" %%i in ('where python.exe 2^>nul') do set PYTHON_PATH=%%i

if "%PYTHON_PATH%"=="" (
    echo ERROR: Python not found in PATH!
    echo Please install Python and add it to the system PATH.
    exit /b 1
)

echo Found Python at: %PYTHON_PATH%
%PYTHON_PATH% --version

echo.
echo Setting up Jenkins environment variables...
echo Add the following to Jenkins System Configuration:
echo PYTHON_HOME=%PYTHON_PATH:python.exe=%
echo PATH=%%PYTHON_HOME%%;%%PATH%%

echo.
echo Configuration complete!
pause
