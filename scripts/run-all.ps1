<#
Start all services for local live development.
Opens three separate PowerShell windows: backend, frontend, monitoring-agent.
Usage: Right-click -> Run with PowerShell, or from an elevated PowerShell prompt:
  .\scripts\run-all.ps1
#>

$root = Split-Path -Parent $MyInvocation.MyCommand.Definition

function Start-ServiceWindow($workdir, $command, $title) {
    $escaped = $command.Replace('"', '`"')
    $args = "-NoExit -Command `"Set-Location -Path '$workdir'; $escaped`""
    Start-Process -FilePath powershell -ArgumentList $args -WindowStyle Normal -WorkingDirectory $workdir -Verb runAs
}

Write-Host "Starting backend, frontend, and monitoring-agent in separate windows..."

$base = (Resolve-Path "$root\..")

$backendDir = Join-Path $base 'backend'
$frontendDir = Join-Path $base 'frontend'
$agentDir = Join-Path $base 'monitoring-agent'

# Backend: use venv python to run uvicorn
$backendCmd = ".\venv\Scripts\python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000"
Start-ServiceWindow $backendDir $backendCmd 'Backend (uvicorn)'

# Frontend: npm dev server
$frontendCmd = "npm run dev"
Start-ServiceWindow $frontendDir $frontendCmd 'Frontend (Vite)'

# Monitoring agent
$agentCmd = ".\venv\Scripts\python agent.py"
Start-ServiceWindow $agentDir $agentCmd 'Monitoring Agent'

Write-Host "Launched windows for backend, frontend, and monitoring agent. Use those windows to view output or Ctrl+C to stop." 
