# Flask + ngrok Setup Script
# This script sets up the virtual environment, installs dependencies, and starts Flask with ngrok

Write-Host "🚀 Flask + ngrok Setup & Runner" -ForegroundColor Cyan
Write-Host "================================`n" -ForegroundColor Cyan

# Navigate to flask folder
$flaskDir = "D:\Fishesh\flask"
Set-Location $flaskDir

# Check if Python is available
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python not found. Please install Python first." -ForegroundColor Red
    exit 1
}

# Create virtual environment if it doesn't exist
if (-not (Test-Path ".venv")) {
    Write-Host "`n📦 Creating virtual environment..." -ForegroundColor Yellow
    python -m venv .venv
    Write-Host "✅ Virtual environment created" -ForegroundColor Green
} else {
    Write-Host "`n✅ Virtual environment already exists" -ForegroundColor Green
}

# Activate virtual environment
Write-Host "`n🔧 Activating virtual environment..." -ForegroundColor Yellow
& ".\.venv\Scripts\Activate.ps1"

# Upgrade pip
Write-Host "`n📦 Upgrading pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip --quiet

# Install dependencies
Write-Host "`n📦 Installing dependencies (flask, flask-cors, pyngrok)..." -ForegroundColor Yellow
pip install flask flask-cors pyngrok --quiet

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Dependencies installed successfully" -ForegroundColor Green
} else {
    Write-Host "❌ Failed to install dependencies" -ForegroundColor Red
    exit 1
}

# Start Flask + ngrok
Write-Host "`n🚀 Starting Flask app with ngrok tunnel..." -ForegroundColor Cyan
Write-Host "================================`n" -ForegroundColor Cyan

python run_with_ngrok.py
