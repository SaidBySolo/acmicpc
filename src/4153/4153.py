while True:
    i = input()
    if i == "0 0 0":
        break
    a,b,c=sorted(map(int, i.split()))
    if (a**2 + b**2) == c**2:
        print("right")
    else:
        print("wrong")
