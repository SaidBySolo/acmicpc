import sys

N, X = map(int, sys.stdin.readline().rstrip().split())

A = list(map(int, sys.stdin.readline().rstrip().split()))

result = ""
for N in A:
    if N < X:
        result += f"{N} "

print(result)
