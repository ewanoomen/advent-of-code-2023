import numpy as np

# rows = columns = 10
rows = columns = 140

# with open("example.txt") as input:
with open("input.txt") as input:
    lines = input.readlines()

matrix = np.array([["."] * columns])

for line in lines:
    line = line.replace("\n", "")
    line_as_list = [c for c in line]

    matrix = np.append(matrix, [line_as_list], 0)

matrix = np.append(matrix, [["."] * columns], 0)
matrix = np.insert(matrix, [0], [["."]], 1)
matrix = np.insert(matrix, [columns+1], [["."]], 1)

print(matrix)

# part 1
# part_numbers = []

# for row in range(1, rows+1):
#     row_indexes = []
#     for cell in range(1, columns+1):
#         current = matrix[row][cell]
#         if not current.isdigit(): continue
#         surrounding = {
#             "topleft": matrix[row-1][cell-1],
#             "top": matrix[row-1][cell],
#             "topright": matrix[row-1][cell+1],
#             "right": matrix[row][cell+1],
#             "bottomright": matrix[row+1][cell+1],
#             "bottom": matrix[row+1][cell],
#             "bottomleft": matrix[row+1][cell-1],
#             "left": matrix[row][cell-1],
#         }
#         for symbol in ["*", "@", "/", "#", "$", "-", "=", "&", "%", "+"]:
#             if symbol in surrounding.values():
#                 indexes = [cell]
#                 for before in range(1, cell):
#                     if matrix[row][cell-before].isdigit():
#                         indexes.insert(0, cell-before)
#                     else:
#                         break
#                 for after in range(1, cell):
#                     if matrix[row][cell+after].isdigit():
#                         indexes.append(cell+after)
#                     else:
#                         break
#                 row_indexes.append(indexes)
#     unique_row_indexes = [list(x) for x in set(tuple(x) for x in row_indexes)]

#     for unique_indexes in unique_row_indexes:
#         part_number = "".join([str(matrix[row][index]) for index in unique_indexes])
#         part_numbers.append(int(part_number))

# print(part_numbers)
# print(sum(part_numbers))

# part 2
gear_ratios = []

for row in range(1, rows+1):
    row_indexes = []
    for cell in range(1, columns+1):
        current = matrix[row][cell]
        if current == "*":
            surrounding = {
                "topleft": matrix[row-1][cell-1],
                "top": matrix[row-1][cell],
                "topright": matrix[row-1][cell+1],
                "right": matrix[row][cell+1],
                "bottomright": matrix[row+1][cell+1],
                "bottom": matrix[row+1][cell],
                "bottomleft": matrix[row+1][cell-1],
                "left": matrix[row][cell-1],
            }
            surrounding_digits = [key for key, value in surrounding.items() if surrounding[key].isdigit()]

            if len(surrounding_digits) > 1:
                location = {
                    "topleft": [row-1, cell-1],
                    "top": [row-1, cell],
                    "topright": [row-1, cell+1],
                    "right": [row, cell+1],
                    "bottomright": [row+1, cell+1],
                    "bottom": [row+1, cell],
                    "bottomleft": [row+1, cell-1],
                    "left": [row, cell-1],
                }
                gear_values = []
                for x in surrounding_digits:
                    digit_row, digit_cell = location[x]
                    gear_value = [matrix[digit_row][digit_cell]]
                    for before in range(1, digit_cell):
                        if matrix[digit_row][digit_cell-before].isdigit():
                            gear_value.insert(0, matrix[digit_row][digit_cell-before])
                        else:
                            break
                    for after in range(1, digit_cell):
                        if matrix[digit_row][digit_cell+after].isdigit():
                            gear_value.append(matrix[digit_row][digit_cell+after])
                        else:
                            break
                    gear_values.append("".join([str(v) for v in gear_value]))
                unique_gear_values = [int(v) for v in set(gear_values)]
                if len(unique_gear_values) == 2:
                    gear_ratio = unique_gear_values[0] * unique_gear_values[1]
                    gear_ratios.append(gear_ratio)

print(gear_ratios)
print(sum(gear_ratios))
