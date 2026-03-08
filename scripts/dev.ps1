Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

Write-Host "Starting API (local dev)..."
Set-Location "$PSScriptRoot\..\api"
.\.venv\Scripts\Activate.ps1
python manage.py migrate
python manage.py runserver 127.0.0.1:8000
