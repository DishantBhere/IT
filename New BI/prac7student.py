#Data Analysis using Pandas (Student Dataset)

import pandas as pd

# CSV file path
file_path = "StudentsPerformance.csv"

# Read CSV file
df = pd.read_csv(file_path)

print("\n================ STUDENT PERFORMANCE DATA ANALYSIS ================\n")


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


print("\n--------------- DATA INSIGHTS ----------------")

print("Average Math Score:", round(df['math score'].mean(), 2))
print("Average Reading Score:", round(df['reading score'].mean(), 2))
print("Average Writing Score:", round(df['writing score'].mean(), 2))

print("\nGender Distribution:")
print(df['gender'].value_counts())

print("\nTest Preparation Course Distribution:")
print(df['test preparation course'].value_counts())

