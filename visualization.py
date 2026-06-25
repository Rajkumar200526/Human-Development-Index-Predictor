import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("dataset/clean_hdi.csv")

# Style
sns.set_style("whitegrid")

print("Dataset Loaded Successfully")
print(df.head())

# -----------------------------
# Create HDI Category
# -----------------------------
def classify(hdi):
    if hdi >= 0.800:
        return "Very High"
    elif hdi >= 0.700:
        return "High"
    elif hdi >= 0.550:
        return "Medium"
    else:
        return "Low"

df["HDI_Category"] = df["HDI"].apply(classify)

# ==========================================================
# 1. Distribution Plot
# ==========================================================

plt.figure(figsize=(8,5))
sns.histplot(df["HDI"], kde=True)
plt.title("Distribution of HDI")
plt.xlabel("HDI")
plt.ylabel("Count")
plt.savefig("graphs/hdi_distribution.png")
plt.close()

# ==========================================================
# 2. Scatter Plot
# ==========================================================

plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x="LifeExpectancy", y="HDI")
plt.title("Life Expectancy vs HDI")
plt.savefig("graphs/life_hdi.png")
plt.close()

# ==========================================================
# 3. Scatter Plot (GNI)
# ==========================================================

plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x="GNI", y="HDI")
plt.title("GNI vs HDI")
plt.savefig("graphs/gni_hdi.png")
plt.close()

# ==========================================================
# 4. Scatter Plot (Schooling)
# ==========================================================

plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x="MeanSchooling", y="HDI")
plt.title("Mean Schooling vs HDI")
plt.savefig("graphs/school_hdi.png")
plt.close()

# ==========================================================
# 5. Strip Plot
# ==========================================================

plt.figure(figsize=(8,5))
sns.stripplot(data=df, x="HDI_Category", y="HDI")
plt.title("HDI Category Strip Plot")
plt.savefig("graphs/stripplot.png")
plt.close()

# ==========================================================
# 6. Box Plot
# ==========================================================

plt.figure(figsize=(6,5))
sns.boxplot(y=df["HDI"])
plt.title("HDI Box Plot")
plt.savefig("graphs/boxplot.png")
plt.close()

# ==========================================================
# 7. Heatmap / Correlation Matrix
# ==========================================================

plt.figure(figsize=(8,6))

corr = df[
    [
        "LifeExpectancy",
        "ExpectedSchooling",
        "MeanSchooling",
        "GNI",
        "HDI"
    ]
].corr()

sns.heatmap(corr, annot=True, cmap="coolwarm")

plt.title("Correlation Matrix")

plt.savefig("graphs/correlation_matrix.png")

plt.close()

# ==========================================================
# 8. Pair Plot
# ==========================================================

pair = sns.pairplot(
    df[
        [
            "LifeExpectancy",
            "ExpectedSchooling",
            "MeanSchooling",
            "GNI",
            "HDI"
        ]
    ]
)

pair.savefig("graphs/pairplot.png")

plt.close()

print("\n==============================")
print("All Graphs Generated Successfully!")
print("==============================")