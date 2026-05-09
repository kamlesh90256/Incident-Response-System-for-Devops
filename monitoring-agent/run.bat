@echo off
REM DevOps Monitoring System - Monitoring Agent Run Script for Windows

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Starting Monitoring Agent
echo Press Ctrl+C to stop
echo.

python agent.py
