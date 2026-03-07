#Data Analysis using Pandas (Employee Dataset)

import pandas as pd

# CSV file path
file_path = "employees.csv"

# Read CSV file
df = pd.read_csv(file_path)

print("\n================ EMPLOYEE DATA ANALYSIS ================\n")


print("--------------- FIRST 5 ROWS OF DATA ----------------")
print(df.head())


print("\n--------------- DATASET INFORMATION ----------------")
df.info()


print("\n--------------- BASIC STATISTICS ----------------")
print(df.describe())


print("\n--------------- MISSING VALUES CHECK ----------------")
print(df.isnull().sum())


print("\n--------------- COLUMN NAMES ----------------")
print(list(df.columns))


print("\n--------------- ADDITIONAL INSIGHTS ----------------")

if 'SALARY' in df.columns:
    print("Average Salary :", round(df['SALARY'].mean(), 2))
    print("Minimum Salary :", df['SALARY'].min())
    print("Maximum Salary :", df['SALARY'].max())

if 'DEPARTMENT_ID' in df.columns:
    print("\nEmployees per Department:")
    print(df['DEPARTMENT_ID'].value_counts())
