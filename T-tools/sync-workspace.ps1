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
    Write-Host "  Checking $repoName..." -ForegroundColor Cyan

    $defaultBranch = git -C $repoPath remote show origin 2>$null |
                     Select-String "HEAD branch" |
                     ForEach-Object { ($_ -split ":\s*")[1].Trim() }
    if (-not $defaultBranch) { $defaultBranch = "main" }

    git -C $repoPath checkout $defaultBranch 2>$null
    git -C $repoPath fetch origin $defaultBranch 2>$null

    $behind = git -C $repoPath rev-list "HEAD..origin/$defaultBranch" --count 2>$null
    if ($behind -eq "0" -or $behind -eq "") {
        Write-Host "  No changes - already up to date" -ForegroundColor DarkGray
        return
    }

    Write-Host "  $behind new commit(s) - pulling..." -ForegroundColor Yellow
    git -C $repoPath pull origin $defaultBranch 2>$null

    $changed = git -C $repoPath diff "HEAD@{1}" HEAD --name-only 2>$null
    if ($changed) {
        Write-Host "  Changed files:" -ForegroundColor Green
        $changed -split "`n" | Where-Object { $_ } | ForEach-Object {
            Write-Host "    $_" -ForegroundColor White
        }
    } else {
        Write-Host "  OK - synced" -ForegroundColor Green
    }
}

Show-Menu
$choice = Read-Host "  Select"

switch ($choice.ToUpper()) {
    "Q" { exit }
    "A" {
        Write-Host ""
        Write-Host "  Checking all repositories..." -ForegroundColor Yellow
        foreach ($repo in $repos) { Sync-Repo $repo }
        Write-Host ""
        Write-Host "  Done." -ForegroundColor Green
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
