import sys

range_value = int(sys.stdin.readline())

for _ in range(range_value):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a + b)
