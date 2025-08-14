import pandas as pd
data = pd.read_csv("data.csv")
df = pd.DataFrame(data)
print(df.to_string())

# df.dropna(inplace=True)
# df.fillna(130, inplace= True) #replacing all the null vlaues 
# df.fillna({"Calories": 130}, inplace=True)
x = df["Calories"].mean()
print(x)
df.fillna({"Calories": x}, inplace=True)
print(df.to_string()) 

x = df["Calories"].mean()
y = df["Calories"].median()
z = df["Calories"].mean()

df.fillna({"Calories": x}, inplace=True)
df.fillna({"Calories": y}, inplace=True)