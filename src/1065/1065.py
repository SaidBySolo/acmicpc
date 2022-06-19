x = int(input())

count = 0


for i in range(1, x + 1):

    if i <= 99:
        count += 1
        continue

    int_list = list(map(int, str(i)))
    length = len(int_list)
    if length == 4:
        if (
            int_list[3] - int_list[2]
            == int_list[2] - int_list[1]
            == int_list[1] - int_list[0]
        ):
            count += 1
    if length == 3:
        if int_list[2] - int_list[1] == int_list[1] - int_list[0]:
            count += 1

print(count)
