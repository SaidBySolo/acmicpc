year = int(input())

if (year / 4).is_integer() and not (year / 100).is_integer():
    print("1")
elif (year / 100).is_integer() and not (year / 400).is_integer():
    print("0")
elif (year / 400).is_integer():
    print("1")
else:
    print("0")
