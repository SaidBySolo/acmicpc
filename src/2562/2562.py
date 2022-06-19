from typing import List


l: List[int] = []

while True:
    if len(l) == 9:
        break
    l.append(int(input()))

print(max(l))
print(l.index(max(l)) + 1)
