@echo off
REM DevOps Monitoring System - Backend Setup Script for Windows

echo ============================================
echo Setting up Backend (FastAPI)
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
echo To start the backend server, run:
echo   venv\Scripts\activate.bat
echo   uvicorn main:app --reload
echo.
pause
