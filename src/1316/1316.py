from typing import List


loop_count = int(input())

inputs: List[str] = []
checked: List[str] = []

for _ in range(loop_count):
    inputs.append(input())


for input in inputs:
    for index, item in enumerate(input, 0):
        if index == 0:
            checked.append(item)
            continue
        if item in checked:
            if checked[index - 1] == item:
                checked.append(item)
                continue
            else:
                loop_count -= 1
                break
        else:
            checked.append(item)
            continue
    checked.clear()

print(loop_count)
