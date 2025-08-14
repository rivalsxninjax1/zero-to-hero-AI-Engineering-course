
import pandas as pd
import numpy as np

# Sample data with duplicates, inconsistent text case, and outliers
data = {
    'Product': ['Laptop', 'laptop', 'Smartphone', 'Tablet', 'Tablet', 'Smartphone'],
    'Price': [1200, 1200, 800, 300, 3000, 850],
    'Quantity': [5, 5, 10, 7, 7, 10]
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

# 1. Remove duplicates (considering all columns)
df = df.drop_duplicates()

# 2. Standardize text data (make all product names lowercase)
df['Product'] = df['Product'].str.lower()

# 3. Handle outliers in Price (e.g., remove prices outside 1.5*IQR range)

Q1 = df['Price'].quantile(0.25)
Q3 = df['Price'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df_no_outliers = df[(df['Price'] >= lower_bound) & (df['Price'] <= upper_bound)]

print("\nData after removing duplicates, standardizing text, and removing outliers:\n", df_no_outliers)
