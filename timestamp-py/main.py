import datetime


s = int(input("Enter time in seconds: "))
x = datetime.datetime.fromtimestamp(s)
print(x.strftime("%H:%M:%S"))
