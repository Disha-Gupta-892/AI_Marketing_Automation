# GitHub Upload Script for Workflow_Automations Repository
# Replace YOUR_USERNAME with your GitHub username before running

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "GitHub Upload Script" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Get GitHub username
$username = Read-Host "Enter your GitHub username"

if ([string]::IsNullOrWhiteSpace($username)) {
    Write-Host "Error: Username cannot be empty" -ForegroundColor Red
    exit 1
}

$repoName = "Workflow_Automations"
$remoteUrl = "https://github.com/$username/$repoName.git"

Write-Host ""
Write-Host "Repository: $repoName" -ForegroundColor Yellow
Write-Host "Remote URL: $remoteUrl" -ForegroundColor Yellow
Write-Host ""

# Check if remote already exists
$existingRemote = git remote get-url origin 2>$null
if ($existingRemote) {
    Write-Host "Updating existing remote..." -ForegroundColor Yellow
    git remote set-url origin $remoteUrl
} else {
    Write-Host "Adding remote..." -ForegroundColor Yellow
    git remote add origin $remoteUrl
}

Write-Host ""
Write-Host "Step 1: Creating repository on GitHub..." -ForegroundColor Cyan
Write-Host "Please go to: https://github.com/new" -ForegroundColor White
Write-Host "Repository name: $repoName" -ForegroundColor White
Write-Host "Don't initialize with README, .gitignore, or license" -ForegroundColor White
Write-Host ""
$continue = Read-Host "Have you created the repository on GitHub? (y/n)"

if ($continue -ne "y" -and $continue -ne "Y") {
    Write-Host "Please create the repository first, then run this script again." -ForegroundColor Yellow
    exit 0
}

Write-Host ""
Write-Host "Step 2: Pushing to GitHub..." -ForegroundColor Cyan

# Rename branch to main if needed
$currentBranch = git branch --show-current
if ($currentBranch -ne "main") {
    Write-Host "Renaming branch to main..." -ForegroundColor Yellow
    git branch -M main
}

# Push to GitHub
Write-Host "Pushing code to GitHub..." -ForegroundColor Yellow
git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "SUCCESS! Code uploaded to GitHub" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "Repository URL: https://github.com/$username/$repoName" -ForegroundColor Cyan
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "Error: Push failed. You may need to:" -ForegroundColor Red
    Write-Host "1. Check your GitHub credentials" -ForegroundColor Yellow
    Write-Host "2. Use a Personal Access Token if prompted for password" -ForegroundColor Yellow
    Write-Host "3. Make sure the repository exists on GitHub" -ForegroundColor Yellow
    Write-Host ""
}

