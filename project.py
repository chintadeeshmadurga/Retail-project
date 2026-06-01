import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("retail.csv")

print("Dataset")
print(df)

print("\nStatistical Summary")
print(df.describe())

# Total Sales
print("\nTotal Sales =", df["Sales"].sum())

# Total Profit
print("Total Profit =", df["Profit"].sum())

# Bar Chart
plt.figure(figsize=(8,5))
sns.barplot(x="Product", y="Sales", data=df)
plt.title("Sales by Product")
plt.xticks(rotation=45)
plt.show()

# Pie Chart
category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(6,6))
plt.pie(category_sales,
        labels=category_sales.index,
        autopct='%1.1f%%')

plt.title("Sales by Category")
plt.show()

# Correlation Heatmap
sns.heatmap(
    df[["Sales","Profit"]].corr(),
    annot=True
)

plt.title("Sales vs Profit Correlation")
plt.show()