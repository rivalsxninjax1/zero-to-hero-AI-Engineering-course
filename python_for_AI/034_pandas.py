import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, None, 22],
    'Salary': [50000, 60000, 65000, 58000, None],
    'Department': ['HR', 'Engineering', 'Marketing', 'HR', 'Engineering']
}

df = pd.DataFrame(data)
# print(df)

#to view the first few rows 
# print(df.head())

#to view the data summery state
# print(df.describe())

#info about the data types and nulls 
# print(df.info())

#SINCE AI cant train on the null value we need to give them vlaues
# filling the null age with  the average age 


df['Age'] = df['Age'].fillna(df['Age'].mean())

# dropping rows  where the salary is missing 
df = df.dropna(subset=['Salary'])
# print(df)

#who earns more than 55000
high_earners = df[df['Salary']> 55000]
# print(high_earners)

#only people from engineering
engineering = df[df['Department'] == 'Engineering']
# print(engineering)

#average salary by department 
avg_salary = df.groupby('Department')['Salary'].mean()
print(avg_salary)