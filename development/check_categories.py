import pandas as pd

# Load dataset
df = pd.read_csv("data/employee_productivity.csv")

print("Dataset loaded successfully!")

print("\nDepartments:")
print(df["Department"].value_counts())

print("\nGender:")
print(df["Gender"].value_counts())

print("\nJob Titles:")
print(df["Job_Title"].value_counts())

print("\nEducation Levels:")
print(df["Education_Level"].value_counts())

print("\nResigned:")
print(df["Resigned"].value_counts())