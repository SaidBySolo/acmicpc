total = input()

L = list(map(int, input().split()))

M = max(L)

average = 0

for N in L:
    average += N / M * 100

print(int(average) / int(total))
