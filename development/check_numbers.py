import pandas as pd

# Load dataset
df = pd.read_csv("data/employee_productivity.csv")

print("Dataset loaded successfully!")

numeric_columns = [
    "Age",
    "Years_At_Company",
    "Performance_Score",
    "Monthly_Salary",
    "Work_Hours_Per_Week",
    "Projects_Handled",
    "Overtime_Hours",
    "Sick_Days",
    "Remote_Work_Frequency",
    "Team_Size",
    "Training_Hours",
    "Promotions",
    "Employee_Satisfaction_Score"
]

print("\nNumerical Data Summary:")
print(df[numeric_columns].describe().round(2))