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

# SESSION 2 - TASK 4

healthy = df[df["target"] == 0]["thalach"]
disease = df[df["target"] == 1]["thalach"]

print("healthy patients:", len(healthy))
print("disease patients:", len(disease))

print("healthy mean:", healthy.mean())
print("disease mean:", disease.mean())

stat, p = stats.mannwhitneyu(healthy, disease)

print("Mann-Whitney U:", stat)
print("P-value:", p)

print("healthy SEM:", stats.sem(healthy))
print("disease SEM:", stats.sem(disease))

means = [healthy.mean(), disease.mean()]
errors = [stats.sem(healthy), stats.sem(disease)]

plt.bar(["Healthy", "Disease"], means, yerr=errors, capsize=5)

plt.ylabel("Maximum Heart Rate (bpm)")
plt.title("Healthy vs Disease: Mean Heart Rate")
plt.show()

plt.savefig("heart_rate_comparison.png")


# SESSION 2 - TASK 5

correlation = df["age"].corr(df["thalach"])

print("Correlation between age and heart rate:", correlation)

plt.scatter(df["age"], df["thalach"])

plt.title("Age vs Maximum Heart Rate")
plt.xlabel("Age (years)")
plt.ylabel("Maximum Heart Rate (bpm)")

plt.savefig("age_vs_heart_rate.png")
plt.show()

# SESSION 2 - TASK 6

chem = pd.read_csv("chemicals_cancer.csv")

print(chem.head())
print(chem.columns)

benzene_corr = chem["benzene"].corr(chem["malignancy"])
cadmium_corr = chem["cadmium"].corr(chem["malignancy"])

print("Benzene correlation:", benzene_corr)
print("Cadmium correlation:", cadmium_corr)

# SESSION 2 - TASK 7

filtered = chem[
    (chem["pollution_index"] > 40) &
    (chem["pollution_index"] < 60)
]

print("Filtered patients:", len(filtered))

print("Benzene correlation:",
      filtered["benzene"].corr(filtered["malignancy"]))

print("Cadmium correlation:",
      filtered["cadmium"].corr(filtered["malignancy"]))
