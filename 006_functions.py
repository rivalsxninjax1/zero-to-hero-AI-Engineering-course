def classify_number(num):
    if num > 0:
        return "Positive"
    elif num <0:
        return "negative"
        
    else:
        return "zero"
    

a = int(input("enter a number"))
print(classify_number(a))
