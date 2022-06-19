from typing import List

from string import ascii_lowercase

i = list(input())
a = list(ascii_lowercase)

result: List[int] = []

for x in a:
    if x in i:
        result.append(i.index(x))
    else:
        result.append(-1)

print(*result)
