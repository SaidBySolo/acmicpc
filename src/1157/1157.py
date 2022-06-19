from collections import Counter

a = Counter(input().lower())
n = a.most_common(1)[0][0].upper()

if list(a.values()).count(max(a.values())) >= 2:
    print("?")
else:
    print(n)
