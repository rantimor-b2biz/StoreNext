# sync-workspace.ps1
# Place at: C:\Users\rant\Documents\ran-workspace\sync-workspace.ps1

$WORKSPACE = "C:\Users\rant\Documents\ran-workspace"
$repos = @("FRACTIONAL_CMO", "Pilgrim-Prayers", "ShelfieTech", "StoreNext")

function Show-Menu {
    Clear-Host
    Write-Host ""
    Write-Host "  === Workspace Sync ===" -ForegroundColor Cyan
    Write-Host ""
    $i = 1
    foreach ($repo in $repos) {
        $repoPath = Join-Path $WORKSPACE $repo
        $branch = git -C $repoPath branch --show-current 2>$null
        $lastCommit = git -C $repoPath log -1 --format="%cr" 2>$null
        if ($branch) {
            Write-Host "  [$i] $repo ($branch, $lastCommit)" -ForegroundColor White
        } else {
            Write-Host "  [$i] $repo" -ForegroundColor White
        }
        $i++
    }
    Write-Host ""
    Write-Host "  [A] Sync all" -ForegroundColor Yellow
    Write-Host "  [Q] Quit" -ForegroundColor Gray
    Write-Host ""
}

function Sync-Repo {
    param($repoName)
    $repoPath = Join-Path $WORKSPACE $repoName
    Write-Host ""
    Write-Host "  Syncing $repoName..." -ForegroundColor Cyan

    $defaultBranch = git -C $repoPath remote show origin 2>$null |
                     Select-String "HEAD branch" |
                     ForEach-Object { ($_ -split ":\s*")[1].Trim() }

    if (-not $defaultBranch) { $defaultBranch = "main" }

    git -C $repoPath checkout $defaultBranch 2>$null
    $result = git -C $repoPath pull origin $defaultBranch 2>&1

    if ($LASTEXITCODE -eq 0) {
        Write-Host "  OK - $repoName ($defaultBranch)" -ForegroundColor Green
    } else {
        Write-Host "  FAIL - $repoName" -ForegroundColor Red
        Write-Host "  $result" -ForegroundColor Red
    }
}

Show-Menu
$choice = Read-Host "  Select"

switch ($choice.ToUpper()) {
    "Q" { exit }
    "A" {
        Write-Host ""
        Write-Host "  Syncing all..." -ForegroundColor Yellow
        foreach ($repo in $repos) { Sync-Repo $repo }
        Write-Host ""
        Write-Host "  All done." -ForegroundColor Green
    }
    default {
        $index = [int]$choice - 1
        if ($index -ge 0 -and $index -lt $repos.Count) {
            Sync-Repo $repos[$index]
        } else {
            Write-Host "  Invalid selection." -ForegroundColor Red
        }
    }
}

Write-Host ""
Read-Host "  Press Enter to exit"
