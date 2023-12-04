import re

f = open("/Users/alinasafina/PycharmProjects/aoc2023/aoc_day_3/input.txt", encoding="UTF-8")
lines = [i.strip() for i in f]
symbols = "*-+=@%$#!&"
result = 0
for line_index, line in enumerate(lines):
    if line_index - 1 >= 0:
        prev_line = line[line_index - 1]
    else:
        prev_line = None
    if line_index + 1 < len(lines):
        next_line = line[line_index + 1]
    else:
        next_line = None
    flag = False
    for number in re.finditer(r'[0-9]+', line):
        first_index, last_index = number.span()
        number = int(number.group())
        left_index = first_index-1 if first_index-1 > 0 else first_index
        right_index = last_index+1 if last_index+1 < len(line) else last_index
        symbol_left = symbol_right = symbol_above = symbol_below = False
        symbol_left = first_index-1 > 0 and line[first_index-1] != '.'
        symbol_right = last_index + 1 < len(line) and line[last_index + 1] != '.'

        if prev_line is not None:
            s = prev_line[left_index:right_index+1]
            symbol_above = re.match("^[0-9.]+$", s) is None
        if next_line is not None:
            s = next_line[left_index:right_index + 1]
            symbol_below = re.match("^[0-9.]+$", s) is None
        if symbol_left or symbol_right or symbol_above or symbol_below:
            result += number
print(result)

