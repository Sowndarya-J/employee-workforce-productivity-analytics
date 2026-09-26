import pandas as pd

# Load dataset
df = pd.read_csv("data/employee_productivity.csv")

# Create training groups
df["Training_Group"] = pd.cut(
    df["Training_Hours"],
    bins=[-1, 25, 50, 75, 100],
    labels=["Low", "Medium", "High", "Very High"]
)

# Create overtime groups
df["Overtime_Group"] = pd.cut(
    df["Overtime_Hours"],
    bins=[-1, 10, 20, 30, float("inf")],
    labels=[
        "Low Overtime",
        "Medium Overtime",
        "High Overtime",
        "Very High Overtime"
    ]
)

# Create satisfaction groups
df["Satisfaction_Group"] = pd.cut(
    df["Employee_Satisfaction_Score"],
    bins=[0, 2, 3, 4, 5],
    labels=[
        "Low Satisfaction",
        "Medium Satisfaction",
        "High Satisfaction",
        "Very High Satisfaction"
    ],
    include_lowest=True
)

# Save analysis-ready dataset
df.to_csv("results/employee_analysis.csv", index=False)

print("Analysis dataset created successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("Saved to: results/employee_analysis.csv")