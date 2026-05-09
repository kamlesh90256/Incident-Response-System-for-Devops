@echo off
REM DevOps Monitoring System - Backend Run Script for Windows

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Starting FastAPI server on http://localhost:8000
echo Press Ctrl+C to stop
echo.

:: Use the venv python executable to run uvicorn to avoid PATH issues
%~dp0venv\Scripts\python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
