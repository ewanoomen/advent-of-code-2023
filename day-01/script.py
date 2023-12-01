# part 1
# with open("input.txt") as input:
#     total = []
#     for line in input.readlines():
#         digits = ""
#         for char in line:
#             if char.isdigit(): digits = digits + char
#         first_last_digit = digits[:1] + digits[-1:]
#         total.append(int(first_last_digit))
#     print(sum(total))

# part 2
def replace_text_digit(line):
    text_digit_mapping = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }
    for text_digit, digit in text_digit_mapping.items():
        line = line.replace(text_digit, digit)
    return line


with open("input.txt") as input:
    total = []
    for line in input.readlines():
        digits = ""
        line = replace_text_digit(line)
        for char in line:
            if char.isdigit(): digits = digits + char
        first_last_digit = digits[:1] + digits[-1:]
        total.append(int(first_last_digit))
    print(total)
    print(sum(total))