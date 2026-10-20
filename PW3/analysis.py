import pandas as pd 

df = pd.read_csv("heart.csv")

print(df.shape)
print(df.head())

variables = df[["age", "chol", "trestbps", "thalach"]]

print(variables.head())


import matplotlib.pyplot as plt

plt.hist(df["age"], bins=15, edgecolor="black")
plt.title("Distribution of Age")
plt.xlabel("Age (years)")
plt.ylabel("Number of patients")
plt.show()

plt.hist(df["chol"], bins=15, edgecolor="black")
plt.title("Distribution of Cholesterol")
plt.xlabel("Cholesterol (mg/dL)")
plt.ylabel("Number of patients")
plt.show()

plt.hist(df["trestbps"], bins=15, edgecolor="black")
plt.title("Distribution of Resting Blood Pressure")
plt.xlabel("Resting Blood Pressure (mmHg)")
plt.ylabel("Number of patients")
plt.show()

plt.hist(df["thalach"], bins=15, edgecolor="black")
plt.title("Distribution of Maximum Heart Rate")
plt.xlabel("Maximum Heart Rate (bpm)")
plt.ylabel("Number of patients")
plt.show()

from scipy import stats

stat, p = stats.shapiro(df["age"].dropna())

print("Age Shapiro-Wilk test:")
print("Statistic:", stat)
print("P-value:", p)

stat, p = stats.shapiro(df["chol"].dropna())

print("Cholesterol Shapiro-Wilk test:")
print("Statistic:", stat)
print("P-value:", p)

stat, p = stats.shapiro(df["trestbps"].dropna())

print("Blood Pressure Shapiro-Wilk test:")
print("Statistic:", stat)
print("P-value:", p)

stat, p = stats.shapiro(df["thalach"].dropna())

print("Maximum Heart Rate Shapiro-Wilk test:")
print("Statistic:", stat)
print("P-value:", p)