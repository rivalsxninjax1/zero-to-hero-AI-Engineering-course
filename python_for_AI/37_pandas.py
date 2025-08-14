import pandas as pd
a = [1, 2, 5]
data = pd.Series(a) # to make data as a series
print(data[0]) # we can also access the data using the index


#code to give your own index

b = [2, 5,6,7]
bata = pd.Series(b, index = ["x", "y", "z","a"])
print(bata["a"])

#we can also make key value pair while creating a series 
calories = {"day1": 420, "day2": 380, "day3": 390}
cata = pd.Series(calories, index=["day1"])
print(cata)
