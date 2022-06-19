import sys

range_value = int(sys.stdin.readline())

for n in list(range(1, range_value + 1))[::-1]:
    print(n)
