a = int(input())
b = list(map(int, input()))

ps = []
result = []

num = ""

for c in b[::-1]:
    e = a * c
    ps.append(e)
    result.append(str(e) + num)
    num += "0"

s = sum(map(int, result))
print(ps[0], ps[1], ps[2], s, sep="\n")
