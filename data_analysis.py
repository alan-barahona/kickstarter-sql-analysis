import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def get_data(query):
    conn = sqlite3.connect('kickstarter.db')
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

query_1 = """
SELECT main_category, COUNT(*) as total_successful
FROM projects
WHERE state = 'successful'
GROUP BY main_category
ORDER BY total_successful DESC
LIMIT 10;
"""
df_success = get_data(query_1)

df_success.plot(x="main_category", y="total_successful", kind="bar", figsize=(10,6), legend=False, color="skyblue")

plt.title("Top 10 Successful Categories (Kickstarter 2018)")
plt.xlabel("Category")
plt.ylabel("Number of Projects")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


query_2 = """
SELECT country, SUM(usd_pledged_real) as total_pledged
FROM projects
GROUP BY country
ORDER BY total_pledged DESC
LIMIT 10;
"""
df_money = get_data(query_2)

df_money.plot(x="country", y="total_pledged", kind="bar", figsize=(10,6), legend=False, color="lightgreen")

plt.title("Top 10 Countries by Total Money Pledged (USD)")
plt.xlabel("Country")
plt.ylabel("Total Pledged (USD)")
plt.xticks(rotation=0) 
plt.tight_layout()
plt.show()