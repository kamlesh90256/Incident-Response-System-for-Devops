<#
Start backend, frontend, and monitoring agent in the background with per-service logs.
Logs are written to .\logs and PIDs to .\state.

Usage:
  powershell -ExecutionPolicy Bypass -File .\scripts\start-live.ps1
#>

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Definition
$workspaceRoot = Resolve-Path (Join-Path $scriptRoot '..')
$logsDir = Join-Path $workspaceRoot 'logs'
$stateDir = Join-Path $workspaceRoot 'state'

New-Item -ItemType Directory -Force -Path $logsDir | Out-Null
New-Item -ItemType Directory -Force -Path $stateDir | Out-Null

function Start-LoggedProcess {
    param(
        [Parameter(Mandatory=$true)][string]$Name,
        [Parameter(Mandatory=$true)][string]$WorkingDirectory,
        [Parameter(Mandatory=$true)][string]$FilePath,
        [Parameter(Mandatory=$true)][string[]]$ArgumentList
    )

    $stdout = Join-Path $logsDir "$Name.out.log"
    $stderr = Join-Path $logsDir "$Name.err.log"
    $pidFile = Join-Path $stateDir "$Name.pid"

    $process = Start-Process -FilePath $FilePath -ArgumentList $ArgumentList -WorkingDirectory $WorkingDirectory -PassThru `
        -RedirectStandardOutput $stdout -RedirectStandardError $stderr -WindowStyle Hidden

    Set-Content -Path $pidFile -Value $process.Id
    Write-Host "$Name started (PID $($process.Id)). Logs: $stdout | $stderr"
}

$backendDir = Join-Path $workspaceRoot 'backend'
$frontendDir = Join-Path $workspaceRoot 'frontend'
$agentDir = Join-Path $workspaceRoot 'monitoring-agent'

Start-LoggedProcess -Name 'backend' -WorkingDirectory $backendDir -FilePath (Join-Path $backendDir 'venv\Scripts\python.exe') `
    -ArgumentList @('-m', 'uvicorn', 'main:app', '--reload', '--host', '0.0.0.0', '--port', '8000')

# Build once and serve the production bundle so the background launcher stays stable.
Start-Process -FilePath 'npm.cmd' -ArgumentList @('run', 'build') -WorkingDirectory $frontendDir -Wait -NoNewWindow
Start-LoggedProcess -Name 'frontend' -WorkingDirectory $frontendDir -FilePath 'npm.cmd' `
    -ArgumentList @('run', 'preview', '--', '--host', '0.0.0.0', '--port', '3000')

Start-LoggedProcess -Name 'monitoring-agent' -WorkingDirectory $agentDir -FilePath (Join-Path $agentDir 'venv\Scripts\python.exe') `
    -ArgumentList @('agent.py')

Write-Host "All services started in background. Use .\scripts\stop-live.ps1 to stop them."
