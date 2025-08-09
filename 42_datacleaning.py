import pandas as pd

# Sample data (simulate loading from CSV)
data = {
    'Name': ['Alice', 'Bob', None, 'David', 'Eve'],
    'Age': [25, None, 30, 22, 29],
    'Email': ['alice@example.com', 'bob@sample', 'charlie@example.com', None, 'eve@example.com'],
    'Signup Date': ['2023-01-10', '2023/02/15', '15-03-2023', '2023-04-01', None]
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

# 1. Handle missing values
df['Name'].fillna('Unknown', inplace=True)           # Fill missing names
df['Age'].fillna(df['Age'].mean(), inplace=True)     # Fill missing ages with average age
df['Signup Date'].fillna('2023-01-01', inplace=True) # Fill missing dates with default

# 2. Fix inconsistent date formats
df['Signup Date'] = pd.to_datetime(df['Signup Date'], errors='coerce')

# 3. Validate emails (simple check for '@')
df['Email Valid'] = df['Email'].apply(lambda x: '@' in str(x))

# 4. Drop rows where critical data is invalid (e.g., invalid email or date)
df_clean = df[df['Email Valid'] & df['Signup Date'].notnull()]

print("\nCleaned Data:\n", df_clean)

