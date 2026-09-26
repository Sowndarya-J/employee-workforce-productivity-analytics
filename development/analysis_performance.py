import pandas as pd

# Load dataset
df = pd.read_csv("data/employee_productivity.csv")

print("Performance Analysis by Department")
print("=" * 40)

department_performance = (
    df.groupby("Department")
      .agg(
          Employees=("Employee_ID", "count"),
          Average_Performance=("Performance_Score", "mean"),
          Average_Work_Hours=("Work_Hours_Per_Week", "mean"),
          Average_Projects=("Projects_Handled", "mean"),
          Average_Overtime=("Overtime_Hours", "mean"),
          Average_Satisfaction=("Employee_Satisfaction_Score", "mean")
      )
      .round(2)
)

print(department_performance)