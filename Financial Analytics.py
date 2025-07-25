import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('financial_data.csv')

# Preview data
print(df.head())

# Basic info
print("\nMissing values:\n", df.isnull().sum())
print("\nDescriptive Stats:\n", df.describe())

# Fill missing values if any
df.fillna(df.mean(numeric_only=True), inplace=True)

# Correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# Top 10 companies by MarketCap
top_marketcap = df.sort_values(by='MarketCap', ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(data=top_marketcap, x='MarketCap', y='Company', palette='viridis')
plt.title("Top 10 Companies by Market Capitalization")
plt.xlabel("Market Cap (in billions)")
plt.ylabel("Company")
plt.show()

# Revenue vs Profit Scatter Plot
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Revenue', y='Profit', hue='Sector')
plt.title("Revenue vs Profit by Sector")
plt.show()
