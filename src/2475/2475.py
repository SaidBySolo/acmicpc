l = map(int, input().split(" "))
t = 0

for i in l:
    t += i * i

print(t % 10)
