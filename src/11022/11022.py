import sys

range_value = int(sys.stdin.readline())

for n in range(range_value):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(f"Case #{n + 1}: {a} + {b} = {a + b}")
