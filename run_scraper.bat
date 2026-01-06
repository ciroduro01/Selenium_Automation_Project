@echo off
:: Set color to bright green for a professional "developer" look
color 0A
title Selenium Automation Pipeline v2.0
cls

echo ===========================================
echo   STARTING AUTOMATED SCRAPING PROCESS
echo ===========================================
echo.

:: 1. Run the Scraper Engine
echo [1/2] Running Selenium Scraper...
py scraper_engine.py

echo.
:: 2. Run the Data Exporter
echo [2/2] Generating Excel Report...
py export_data.py

echo.
echo ===========================================
echo   PROCESS COMPLETE! 
echo ===========================================
echo.
echo Check your folder for: 
echo - portfolio_data.db 
echo - Scraping_Report.xlsx
echo.
pause