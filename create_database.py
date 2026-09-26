import pandas as pd
import sqlite3

# Load dataset
df = pd.read_csv("data/employee_productivity.csv")

# Connect to SQLite database
connection = sqlite3.connect("employee_productivity.db")

# Store dataframe as SQL table
df.to_sql(
    "employee_productivity",
    connection,
    if_exists="replace",
    index=False
)

# Close database connection
connection.close()

# Display success messages
print("Database created successfully!")
print("Table created: employee_productivity")
print("Total records:", len(df))