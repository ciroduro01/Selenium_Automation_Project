import sqlite3
import logging
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Professional Logging Setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [INFO] %(message)s',
    datefmt='%H:%M:%S',
    handlers=[logging.StreamHandler()]
)

class IndependentScraper:
    def __init__(self, db_name="portfolio_data.db"):
        self.db_name = db_name
        self._init_db()
        self.driver = self._setup_driver()

    def _setup_driver(self):
        options = Options()
        # Suppress browser noise
        options.add_argument("--log-level=3") 
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        prefs = {
            "profile.default_content_setting_values.notifications": 2,
            "profile.default_content_setting_values.geolocation": 2
        }
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--window-size=1920,1080")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
        
        service = Service() 
        return webdriver.Edge(service=service, options=options)

    def _init_db(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS scraped_items (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            source_url TEXT,
                            title TEXT,
                            timestamp DATETIME)''')

    def run_task(self, target_url):
        try:
            logging.info(f"Initializing Session: {target_url}")
            self.driver.get(target_url)
            
            print("\n" + "="*60)
            print(" ACTION REQUIRED FOR LIVE RECORDING:")
            print(" 1. Go to the Edge window.")
            print(" 2. Search for 'Apple' (or any topic) and click it.")
            print(" 3. Wait for the new page to load completely.")
            print(" 4. Come back here and press ENTER.")
            print("="*60 + "\n")
            
            # THE PAUSE: The script stops here while you navigate in the browser
            input(">>> Press ENTER once you have reached your target article...")
            
            # --- THE RE-SYNC LOGIC ---
            # We wait 1 second to ensure the browser's internal 'title' property 
            # has finished updating after the manual navigation.
            time.sleep(1) 
            
            # Re-fetch the Title and URL at this exact moment
            current_title = str(self.driver.title)
            current_url = str(self.driver.current_url)
            
            logging.info(f"Final Destination Captured: {current_title}")
            
            self._save_to_sqlite(current_url, current_title)
            
        except Exception as e:
            logging.error(f"Error during automation: {str(e)}")
        finally:
            self.driver.quit()
            logging.info("Automation pipeline closed successfully.")

    def _save_to_sqlite(self, url, title):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.execute("INSERT INTO scraped_items (source_url, title, timestamp) VALUES (?, ?, ?)", 
                             (url, title, now))
            logging.info("Data successfully persisted to SQLite database.")
        except sqlite3.Error as e:
            logging.error(f"Database error: {e}")

if __name__ == "__main__":
    bot = IndependentScraper()
    bot.run_task("https://www.wikipedia.org")