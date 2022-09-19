import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))
x1 = datetime.datetime(2020, 5, 17)
print(x1)
x2 = datetime.datetime(2018, 6, 1)
print(x2.strftime("%B"))