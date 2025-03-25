# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load sample data (you can replace this with your own dataset)
# Example dataset: Titanic dataset
data = sns.load_dataset('titanic')

# Display basic information about the dataset
print("Dataset Info:")
print(data.info())
print("\nFirst 5 Rows of the Dataset:")
print(data.head())

# ------------------------------
# Data Presentation Section
# ------------------------------

# 1. Summary Statistics
print("\nSummary Statistics:")
print(data.describe(include='all'))

# 2. Bar Plot - Gender Distribution
plt.figure(figsize=(8, 5))
sns.countplot(x='sex', data=data, palette='pastel')
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# 3. Line Plot - Age vs. Fare
plt.figure(figsize=(10, 6))
sns.lineplot(x='age', y='fare', data=data, marker='o', color='green')
plt.title('Age vs. Fare')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.grid(True)
plt.show()

# 4. Scatter Plot - Age vs. Fare by Survival
plt.figure(figsize=(10, 6))
sns.scatterplot(x='age', y='fare', hue='survived', data=data, palette='coolwarm')
plt.title('Age vs. Fare by Survival')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.legend(title='Survived', labels=['No', 'Yes'])
plt.show()

# 5. Correlation Heatmap
plt.figure(figsize=(10, 8))
correlation = data.corr(numeric_only=True)
sns.heatmap(correlation, annot=True, fmt=".2f", cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

# 6. Pie Chart - Class Distribution
class_counts = data['class'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(class_counts, labels=class_counts.index, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99'])
plt.title('Class Distribution')
plt.show()
