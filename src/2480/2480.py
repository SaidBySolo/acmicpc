l=list(map(int, input().split()))
for i in l:
    if l.count(i) == 2:
        r = 1000 + i *100
        break
    elif l.count(i) == 3:
        r = 10000 + i * 1000
        break
    else:
        r = max(l) * 100
print(r)
