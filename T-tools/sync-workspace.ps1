# sync-workspace.ps1
# Place this file at: C:\Users\rant\Documents\ran-workspace\sync-workspace.ps1

$WORKSPACE = "C:\Users\rant\Documents\ran-workspace"

# ── Find all git repos in workspace ──────────────────────────────────────────
$repos = Get-ChildItem -Path $WORKSPACE -Directory |
         Where-Object { Test-Path (Join-Path $_.FullName ".git") } |
         Select-Object -ExpandProperty Name

if ($repos.Count -eq 0) {
    Write-Host ""
    Write-Host "  No git repositories found in $WORKSPACE" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit
}

# ── Display menu ─────────────────────────────────────────────────────────────
function Show-Menu {
    Clear-Host
    Write-Host ""
    Write-Host "  ╔══════════════════════════════════════╗" -ForegroundColor Cyan
    Write-Host "  ║       Workspace Sync — ran-workspace ║" -ForegroundColor Cyan
    Write-Host "  ╚══════════════════════════════════════╝" -ForegroundColor Cyan
    Write-Host ""

    $i = 1
    foreach ($repo in $repos) {
        # Check current branch and last commit
        $repoPath = Join-Path $WORKSPACE $repo
        $branch = git -C $repoPath branch --show-current 2>$null
        $lastCommit = git -C $repoPath log -1 --format="%cr" 2>$null
        Write-Host "  [$i] $repo" -ForegroundColor White -NoNewline
        if ($branch) {
            Write-Host "  ($branch — $lastCommit)" -ForegroundColor DarkGray
        } else {
            Write-Host ""
        }
        $i++
    }

    Write-Host ""
    Write-Host "  [A] Sync all repositories" -ForegroundColor Yellow
    Write-Host "  [Q] Quit" -ForegroundColor DarkGray
    Write-Host ""
}

# ── Sync a single repo ────────────────────────────────────────────────────────
function Sync-Repo {
    param($repoName)

    $repoPath = Join-Path $WORKSPACE $repoName
    Write-Host ""
    Write-Host "  Syncing $repoName..." -ForegroundColor Cyan

    # Detect default branch (main or master)
    $defaultBranch = git -C $repoPath remote show origin 2>$null |
                     Select-String "HEAD branch" |
                     ForEach-Object { ($_ -split ":\s*")[1].Trim() }

    if (-not $defaultBranch) { $defaultBranch = "main" }

    git -C $repoPath checkout $defaultBranch 2>$null
    $result = git -C $repoPath pull origin $defaultBranch 2>&1

    if ($LASTEXITCODE -eq 0) {
        Write-Host "  OK  $repoName ($defaultBranch)" -ForegroundColor Green
    } else {
        Write-Host "  FAIL  $repoName — $result" -ForegroundColor Red
    }
}

# ── Main loop ────────────────────────────────────────────────────────────────
Show-Menu
$choice = Read-Host "  Select"

switch ($choice.ToUpper()) {
    "Q" { exit }
    "A" {
        Write-Host ""
        Write-Host "  Syncing all repositories..." -ForegroundColor Yellow
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
