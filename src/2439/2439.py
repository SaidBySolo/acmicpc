import sys

range_value = int(sys.stdin.readline())

star = ""
for n in list(range(1, range_value + 1))[::-1]:
    a = (n - 1) * " "
    star += "*"
    print(a + star)
