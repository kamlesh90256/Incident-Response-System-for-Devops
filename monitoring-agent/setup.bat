@echo off
REM DevOps Monitoring System - Monitoring Agent Setup Script for Windows

echo ============================================
echo Setting up Monitoring Agent
echo ============================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.11+ from https://www.python.org/
    pause
    exit /b 1
)

echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo ============================================
echo Setup Complete!
echo ============================================
echo.
echo To start the monitoring agent, run:
echo   venv\Scripts\activate.bat
echo   python agent.py
echo.
pause
