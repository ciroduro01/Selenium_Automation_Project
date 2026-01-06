import sqlite3
import pandas as pd
import os

def export_db_to_excel(db_name="portfolio_data.db", output_file="Scraping_Report.xlsx"):
    if not os.path.exists(db_name):
        print(f"Error: Could not find '{db_name}'.")
        return

    try:
        conn = sqlite3.connect(db_name)
        # We add "ORDER BY id DESC" to see the newest items first
        query = "SELECT * FROM scraped_items ORDER BY id DESC"
        df = pd.read_sql_query(query, conn)
        conn.close()

        if df.empty:
            print(f"The database is empty.")
        else:
            df.to_excel(output_file, index=False)
            print(f"SUCCESS! {output_file} created with {len(df)} entries.")
            print("Showing latest capture:")
            print(df.head(1)[['title', 'timestamp']]) # Preview the top result

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    export_db_to_excel()