mapping = {
    "ABC": 2,
    "DEF": 3,
    "GHI": 4,
    "JKL": 5,
    "MNO": 6,
    "PQRS": 7,
    "TUV": 8,
    "WXYZ": 9,
}

result = 0

for i in list(input()):
    for k, v in mapping.items():
        if i in k:
            result += v + 1

print(result)
