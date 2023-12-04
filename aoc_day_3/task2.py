import collections
import re

f = open("/Users/alinasafina/PycharmProjects/aoc2023/aoc_day_3/input.txt", encoding="UTF-8")
lines = [i.strip() for i in f]
result = 0
gears = collections.defaultdict(list)
for line_index, line in enumerate(lines):
    prev_line = lines[line_index-1] if line_index - 1 >= 0 else None
    next_line = lines[line_index+1] if line_index + 1 < len(lines) else None
    for number in re.finditer(r'[0-9]+', line):
        first_index, last_index = number.span()
        last_index = last_index-1

        number = int(number.group())
        left_index = first_index-1 if first_index-1 >= 0 else first_index
        if line[left_index] == "*":
            gears[(left_index, line_index)].append(number)

        right_index = last_index+1 if last_index+1 < len(line) else last_index
        if line[right_index] == "*":
            gears[(right_index, line_index)].append(number)

        if prev_line is not None:
            for index in range(left_index, right_index+1):
                if prev_line[index] == "*":
                    gears[(index, line_index-1)].append(number)
        if next_line is not None:
            for index in range(left_index, right_index + 1):
                if next_line[index] == "*":
                    gears[(index, line_index + 1)].append(number)
for gear in gears.values():
    if len(gear) == 2:
        result += gear[0] * gear[1]
print(result)

