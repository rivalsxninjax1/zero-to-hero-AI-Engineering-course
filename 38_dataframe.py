import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}


#locating rows 
# print(df.loc[0])

#we can also give our own index on the data frame 
df = pd.DataFrame(data, index=["a","b","c"])

# print(df)
# print(df.loc["a"])

