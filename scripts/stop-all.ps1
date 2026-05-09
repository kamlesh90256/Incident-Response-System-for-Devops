<#
Stop services started by run-all.ps1 by terminating processes whose command lines
reference this workspace. This is a best-effort stop; verify critical processes before killing.
Usage: .\scripts\stop-all.ps1
#>

$root = (Resolve-Path "$(Split-Path -Parent $MyInvocation.MyCommand.Definition)\..")
$workspacePath = $root.Path

Write-Host "Stopping processes that reference workspace path: $workspacePath"

# Find processes where CommandLine contains the workspace path (uvicorn/python/node)
$currentPid = $PID
$procs = Get-CimInstance Win32_Process | Where-Object {
    $_.ProcessId -ne $currentPid -and $_.CommandLine -and $_.CommandLine -like "*$workspacePath*"
}

if (-not $procs) {
    Write-Host "No matching processes found."
    exit 0
}

foreach ($p in $procs) {
    try {
        Write-Host "Stopping PID $($p.ProcessId): $($p.CommandLine)"
        Stop-Process -Id $p.ProcessId -Force -ErrorAction Stop
    } catch {
        Write-Warning "Failed to stop PID $($p.ProcessId): $_"
    }
}

Write-Host "Stop attempt complete. Verify services are stopped (ports 8000/3000)."
