age = int(input("Enter your age: "))
 
if age<18:
    print("minor")
elif age<60 and age >=18:
    print("adult")
else:
    print("senior")