# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_excel("Cleaned_Dataset.xlsx")

# 1. Basic Information

print("Dataset Shape:", df.shape)
print("\nColumns:\n", df.columns)
print("\nData Info:")
print(df.info())

# 2. Missing Values Check

print("\nMissing Values:\n")
print(df.isnull().sum())

# 3. Statistical Summary

print("\nStatistical Summary:\n")
print(df.describe())

# 4. Pairplot

corr = df.corr(numeric_only=True)

plt.figure(figsize=(10, 6))

sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)

plt.title("Relationship Between Variables")

plt.tight_layout()
plt.show()

# 5. Distribution Plot

axes = df.hist(figsize=(18,10), bins=20)

for ax in axes.flatten():
    ax.tick_params(axis='x', labelrotation=45)
    ax.margins(x=0.2)

plt.suptitle("Feature Distributions", y=1.0, fontsize=16)

plt.subplots_adjust(
    hspace=0.9,
    wspace=0.2,
    top=0.88,   
    bottom=0.2
)

plt.show()

# 6. Value Counts (first categorical column)

cat_cols = df.select_dtypes(include=['object', 'string']).columns

if len(cat_cols) > 0:
    col = cat_cols[0]
    df[col].value_counts().head(10).plot(kind='bar')
    plt.title(f"Top Categories in {col}")
    plt.show()

# 7. Outlier Detection (Boxplot)

num_cols = df.select_dtypes(include='number').columns

if len(num_cols) > 0:
    plt.figure(figsize=(10,5))
    sns.boxplot(data=df[num_cols])
    plt.title("Outlier Detection")
    plt.xticks(rotation=45)
    plt.show()