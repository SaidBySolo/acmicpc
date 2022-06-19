for _ in range(int(input())):
    i = input().split()

    R = int(i[0])

    S = i[1]

    print("".join([x * R for x in list(S)]))
