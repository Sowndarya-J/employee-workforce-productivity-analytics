import pandas as pd

# Load dataset
df = pd.read_csv("data/employee_productivity.csv")

# Create training groups
df["Training_Group"] = pd.cut(
    df["Training_Hours"],
    bins=[-1, 25, 50, 75, 100],
    labels=["Low", "Medium", "High", "Very High"]
)

# Analyze performance by training group
training_analysis = (
    df.groupby("Training_Group", observed=True)
      .agg(
          Employees=("Employee_ID", "count"),
          Avg_Training_Hours=("Training_Hours", "mean"),
          Avg_Performance=("Performance_Score", "mean"),
          Avg_Satisfaction=("Employee_Satisfaction_Score", "mean")
      )
      .round(2)
)

print("Training vs Performance Analysis")
print("=" * 40)
print(training_analysis)