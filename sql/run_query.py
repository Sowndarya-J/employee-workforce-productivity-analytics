import sqlite3
import pandas as pd

connection = sqlite3.connect("employee_productivity.db")

query = """
SELECT
    CASE
        WHEN Training_Hours < 25 THEN 'Low Training'
        WHEN Training_Hours < 50 THEN 'Medium Training'
        WHEN Training_Hours < 75 THEN 'High Training'
        ELSE 'Very High Training'
    END AS Training_Level,

    COUNT(*) AS Employee_Count,

    ROUND(AVG(Training_Hours), 2) AS Avg_Training_Hours,

    ROUND(AVG(Performance_Score), 2) AS Avg_Performance_Score

FROM employee_productivity

GROUP BY Training_Level

ORDER BY Avg_Training_Hours;
"""

df = pd.read_sql_query(query, connection)

connection.close()

df.to_csv("results/training_analysis.csv", index=False)

print("Training analysis completed!")
print(df)
print("\nSaved to: results/training_analysis.csv")