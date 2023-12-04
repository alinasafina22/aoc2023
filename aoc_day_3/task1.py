import re

f = open("/Users/alinasafina/PycharmProjects/aoc2023/aoc_day_3/input.txt", encoding="UTF-8")
lines = [i.strip() for i in f]
symbols = "*-+=@%$#!&"
result = 0
for line_index, line in enumerate(lines):
    prev_line = lines[line_index-1] if line_index - 1 >= 0 else None
    next_line = lines[line_index+1] if line_index + 1 < len(lines) else None
    for number in re.finditer(r'[0-9]+', line):
        first_index, last_index = number.span()
        last_index = last_index-1

        left_index = first_index-1 if first_index-1 >= 0 else first_index
        right_index = last_index+1 if last_index+1 < len(line) else last_index

        symbol_left = symbol_right = symbol_above = symbol_below = False

        symbol_left = first_index-1 >= 0 and line[first_index-1] != '.'
        symbol_right = last_index + 1 < len(line) and line[last_index + 1] != '.'

        if prev_line is not None:
            s = prev_line[left_index:right_index + 1]
            symbol_above = re.match("^[0-9.]+$", s) is None
        if next_line is not None:
            s = next_line[left_index:right_index + 1]
            symbol_below = re.match("^[0-9.]+$", s) is None
        if symbol_left or symbol_right or symbol_above or symbol_below:
            result += int(number.group())
print(result)

