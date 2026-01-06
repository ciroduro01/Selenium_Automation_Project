# Autonomous Web Intelligence & SQL Reporting Pipeline

A professional-grade Selenium automation system designed for Microsoft Edge. This tool allows for a "Human-in-the-loop" workflow: the automation handles the initial navigation and technical overhead, while the user can perform manual searches or complex interactions before the system captures and persists the final data.

## Technical Stack
- **Engine:** Python 3.13
- **Automation:** Selenium WebDriver (Edge Chromium)
- **Database:** SQLite3 (Relational Persistence)
- **Data Processing:** Pandas & OpenPyXL
- **Interface:** Windows Batch (.bat) CLI
- **Report Viewer:** Compatible with Microsoft Excel / LibreOffice Calc

## Key Features
- **Interactive Capture:** Specifically designed for live demos; the engine pauses to allow for manual navigation (e.g., searching for specific articles) before capturing the final page state.
- **Dynamic Re-Sync:** Implements a post-navigation handshake to ensure the 'Title' and 'URL' properties are accurately retrieved after the user interacts with the browser.
- **One-Click Execution:** Operates via a custom `.bat` launcher—no coding knowledge required to run the full ETL (Extract, Transform, Load) cycle.
- **Relational Storage:** Uses an integrated SQLite database to maintain a historical record of all captured data.
- **Stakeholder-Ready Reporting:** Automatically generates a formatted `.xlsx` report from the local database using Pandas.

## Project Structure
- `scraper_engine.py`: Core automation engine with re-sync capture logic.
- `export_data.py`: Data transformation script that converts SQL records to Excel.
- `run_scraper.bat`: Master orchestration script with a professional CLI theme.
- `portfolio_data.db`: Relational database file (generated on first run).
- `Scraping_Report.xlsx`: Final business-ready output report.

## How to Use
1. Ensure Python 3.13+ is installed.
2. Run `py -m pip install -r requirements.txt` to install dependencies.
3. Double-click `run_scraper.bat`.
4. Navigate to your target page in the Edge window, then press **ENTER** in the console to capture the data.