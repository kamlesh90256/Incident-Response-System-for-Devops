<#
Stop services started by start-live.ps1 using stored pid files.

Usage:
  powershell -ExecutionPolicy Bypass -File .\scripts\stop-live.ps1
#>

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Definition
$workspaceRoot = Resolve-Path (Join-Path $scriptRoot '..')
$stateDir = Join-Path $workspaceRoot 'state'

if (-not (Test-Path $stateDir)) {
    Write-Host "No state directory found; nothing to stop."
    exit 0
}

$pidFiles = Get-ChildItem -Path $stateDir -Filter '*.pid' -ErrorAction SilentlyContinue

if (-not $pidFiles) {
    Write-Host "No pid files found; nothing to stop."
    exit 0
}

foreach ($pidFile in $pidFiles) {
    $name = $pidFile.BaseName
    $processIdText = (Get-Content $pidFile.FullName | Select-Object -First 1).Trim()
    if ([string]::IsNullOrWhiteSpace($processIdText)) {
        continue
    }

    try {
        $processId = [int]$processIdText
        Write-Host "Stopping $name (PID $processId)"
        Stop-Process -Id $processId -Force -ErrorAction Stop
    } catch {
        Write-Warning "Failed to stop $name (PID $processIdText): $_"
    }
}

Write-Host "Stop request complete."
