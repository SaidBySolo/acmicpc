total = int(input())

for _ in range(total):
    test_case = list(map(int, list(input().split())))
    test_case_total = test_case.pop(0)
    average = sum(test_case) / test_case_total
    print(
        f"{round(len(list(filter(lambda x: x > int(average), test_case)))/ test_case_total * 100, 3):.3f}%"
    )
