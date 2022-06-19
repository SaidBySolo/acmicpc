input_value = input()

cycle = 1

if len(input_value) == 1:
    C = 0
    D = int(input_value)
else:
    C, D = map(int, tuple(input_value))


while True:
    result = str(C + D)
    if len(result) == 1:
        new_var = str(D) + result
    else:
        E, F = map(int, tuple(result))
        new_var = str(D) + str(F)

    C, D = map(int, tuple(new_var))

    if len(input_value) == 1:
        G, H = map(int, tuple(f"{C}{D}"))

        if str(D) == input_value and str(G + H) == input_value:
            print(cycle)
            break
        else:
            cycle += 1
    else:
        if str(C) + str(D) == input_value:
            print(cycle)
            break
        else:
            cycle += 1
