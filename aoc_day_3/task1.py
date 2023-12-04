import re

f = open("/Users/alinasafina/PycharmProjects/aoc2023/aoc_day_3/input.txt", encoding="UTF-8")
lines = [i.strip() for i in f]
symbols = "*-+=@%$#!&"
result = 0
for line_index, line in enumerate(lines):
    if line_index - 1 >= 0:
        prev_line = line[line_index - 1]
    else:
        prev_line = line
    if line_index + 1 < len(lines):
        next_line = line[line_index + 1]
    else:
        next_line = line
    flag = False
    for number in re.finditer(r'[0-9]+', line):
        first_index, last_index = number.span()
        number = int(number.group())
        left_index = first_index-1 if first_index-1 > 0 else first_index
        right_index = last_index+1 if last_index+1 < len(line) else last_index
        bottom_and_top_indexes = [i for i in range(first_index-1, last_index+1)]

        if flag:
            result += number
print(result)

