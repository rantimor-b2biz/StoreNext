@echo off
title StoreNext — Sync Main
cd /d "C:\Users\rant\Documents\ran-workspace\StoreNext"
echo.
echo Syncing StoreNext main branch...
echo.
git checkout main
git pull origin main
echo.
echo Done. StoreNext is up to date.
echo.
pause
