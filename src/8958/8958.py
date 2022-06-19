total = int(input())


for _ in range(total):
    stack = 0
    total_stack = 0
    for result in list(input()):
        if result == "O":
            stack += 1
            total_stack += stack
        else:
            stack = 0
    print(total_stack)
