@echo off
REM DevOps Monitoring System - Frontend Setup Script for Windows

echo ============================================
echo Setting up Frontend (React + Vite)
echo ============================================

REM Check if Node.js is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Node.js is not installed or not in PATH
    echo Please install Node.js 18+ from https://nodejs.org/
    pause
    exit /b 1
)

echo Installing dependencies...
call npm install

echo.
echo ============================================
echo Setup Complete!
echo ============================================
echo.
echo To start the frontend development server, run:
echo   npm run dev
echo.
pause
