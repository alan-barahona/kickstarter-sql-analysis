import pandas as pd
import sqlite3

csv_file = 'ks-projects-201801.csv'

print("Loading data.... please wait.")
try:
    df = pd.read_csv(csv_file)
    
    conn = sqlite3.connect('kickstarter.db')
    
    df.to_sql('projects', conn, if_exists='replace', index=False)
    
    print("Success! 'kickstarter.db' has been created.")
    conn.close()
except FileNotFoundError:
    print(f"Error: {csv_file} not found.")