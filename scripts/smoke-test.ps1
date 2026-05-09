<#
Simple smoke test script that checks backend health and frontend root.
Usage: powershell -ExecutionPolicy Bypass -File .\scripts\smoke-test.ps1
#>

param(
    [string]$BackendUrl = 'http://localhost:8000',
    [string]$FrontendUrl = 'http://127.0.0.1:3000'
)

Write-Host "Checking backend health: $BackendUrl/health"
try {
    $b = Invoke-WebRequest -Uri "$BackendUrl/health" -UseBasicParsing -TimeoutSec 5
    Write-Host "Backend OK:" $b.Content
} catch {
    Write-Error "Backend health check failed: $_"
}

Write-Host "Checking frontend root: $FrontendUrl/"
try {
    $f = Invoke-WebRequest -Uri "$FrontendUrl/" -UseBasicParsing -TimeoutSec 5
    Write-Host "Frontend status:" $f.StatusCode
} catch {
    Write-Error "Frontend check failed: $_"
}

# Simple API checks
Write-Host "Checking API base path: $BackendUrl/api/v1"
try {
    $r = Invoke-WebRequest -Uri "$BackendUrl/api/v1" -UseBasicParsing -TimeoutSec 5
    Write-Host "API base responded with status:" $r.StatusCode
} catch {
    Write-Host "API base may not be a browsable endpoint; that's OK if /docs is available."
}

Write-Host "Smoke test complete."
