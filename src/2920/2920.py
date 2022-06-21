from string import digits


ascending = digits[1:9]
decending = ascending[::-1]

i = input()
replaced = i.replace(" ", "")

if replaced == ascending:
    print("ascending")
elif replaced == decending:
    print("descending")
else:
    print("mixed")

