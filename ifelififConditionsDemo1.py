sal=input("My Salry is :")
print(type(sal))
sal=int(sal)
if sal>50000:
    print("You are Eligible for Car loan")
    if sal>80000:
        print("You are eligible for Home loan")
        if sal>100000:
            print("You are Premium Customer: Eligible for all kind of loans & facilities")
else:
    print("Sorry, We can't serve you.")




