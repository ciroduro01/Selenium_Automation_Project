import sqlite3
import json

def export_db_to_json(db_name="portfolio_data.db", output_file="data.json"):
    try:
        conn = sqlite3.connect(db_name)
        conn.row_factory = sqlite3.Row  # This allows us to access columns by name
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM scraped_items")
        rows = cursor.fetchall()
        
        # Convert rows to a list of dictionaries
        data = [dict(row) for row in rows]
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
            
        print(f"SUCCESS: {len(data)} items exported to {output_file} for D3.js")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    export_db_to_json()