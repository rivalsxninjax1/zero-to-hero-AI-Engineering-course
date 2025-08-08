import pandas as pd
data = pd.read_csv("data.csv")
df = pd.DataFrame(data)
# print(df)

#to print the entire data we need to use to_strint( method)
# print(df.to_string())
print(pd.options.display.max_rows)
pd.options.display.max_rows = 999
print(pd.options.display.max_rows)
print(df)