param(
  [switch]$SecretScan
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

if ($SecretScan) {
  $patterns = @(
    "AKIA[0-9A-Z]{16}",
    "-----BEGIN (RSA|EC|OPENSSH) PRIVATE KEY-----",
    "xox[baprs]-[0-9a-zA-Z-]{10,48}",
    "ghp_[0-9A-Za-z]{36}",
    "AIza[0-9A-Za-z\-_]{35}",
    "password\s*=\s*['""][^'""]+['""]",
    "api[_-]?key\s*=\s*['""][^'""]+['""]",
    "secret\s*=\s*['""][^'""]+['""]"
  )

  $hits = @()

  Get-ChildItem -Recurse -File -Force -Path . |
    Where-Object { $_.FullName -notmatch "\\node_modules\\|\\\.git\\|\\\.venv\\|\\dist\\|\\\.angular\\" } |
    ForEach-Object {
      $content = Get-Content -LiteralPath $_.FullName -Raw -ErrorAction SilentlyContinue
      if ($null -ne $content) {
        foreach ($p in $patterns) {
          if ($content -match $p) {
            $hits += "Potential secret pattern '$p' in $($_.FullName)"
          }
        }
      }
    }

  if ($hits.Count -gt 0) {
    Write-Host "Secret scan failed:"
    $hits | ForEach-Object { Write-Host $_ }
    exit 1
  }

  Write-Host "Secret scan passed."
  exit 0
}

$required = @(
  ".\api",
  ".\client",
  ".\infra\postgres",
  ".\docs\adr",
  ".\scripts",
  ".\ai_governance\evaluations"
)

$missing = @()
foreach ($r in $required) {
  if (-not (Test-Path $r)) { $missing += $r }
}

if ($missing.Count -gt 0) {
  Write-Host "Missing required paths:"
  $missing | ForEach-Object { Write-Host $_ }
  exit 1
}

Write-Host "Structure looks OK."
