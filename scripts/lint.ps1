Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

Set-Location "$PSScriptRoot\.."

Write-Host "Python lint..."
.\api\.venv\Scripts\Activate.ps1
flake8

Write-Host "Frontend lint..."
Set-Location ".\client"
npm run lint
