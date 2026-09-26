import pandas as pd

# Load dataset
df = pd.read_csv("data/employee_productivity.csv")

# Calculate department productivity metrics
productivity = (
    df.groupby("Department")
      .agg(
          Employees=("Employee_ID", "count"),
          Avg_Work_Hours=("Work_Hours_Per_Week", "mean"),
          Avg_Projects=("Projects_Handled", "mean"),
          Avg_Overtime=("Overtime_Hours", "mean"),
          Avg_Performance=("Performance_Score", "mean")
      )
)

# Descriptive productivity indicator
productivity["Projects_Per_Work_Hour"] = (
    productivity["Avg_Projects"] / productivity["Avg_Work_Hours"]
)

productivity = productivity.round(3)

print("Employee Productivity Analysis")
print("=" * 40)
print(productivity)