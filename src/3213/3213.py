# https://hsin.hr/2004/regional/seniors/test_data.zip

from math import ceil

i = input()

result: list[str] = []

for _ in range(int(i)):
    result.append(input())

half_piece = result.count("1/2")
quarter_one_piece = result.count("1/4")
quarter_triple_piece = result.count("3/4")

full_piece = 0

original_half_piece = half_piece / 2
full_piece += ceil(original_half_piece)

total = quarter_one_piece + quarter_triple_piece

if quarter_one_piece and quarter_triple_piece:
    if quarter_one_piece > quarter_triple_piece:
        piece = quarter_one_piece - quarter_triple_piece
        quarter_one_piece = piece
        # idk why this is need
        if quarter_one_piece == 1 and not original_half_piece.is_integer():
            quarter_one_piece = 0
        quarter_triple_piece = 0
    elif quarter_one_piece < quarter_triple_piece:
        piece = quarter_triple_piece - quarter_one_piece
        quarter_triple_piece = piece
        quarter_one_piece = 0
    else:
        piece = 0
        quarter_one_piece = 0
        quarter_triple_piece = 0

    full_piece += ceil((total - piece) / 2)

full_piece += ceil(quarter_one_piece / 4)
full_piece += quarter_triple_piece
print(full_piece)
