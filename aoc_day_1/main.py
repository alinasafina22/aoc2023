import re

f = open("/Users/alinasafina/PycharmProjects/aoc2023/aoc_day_1/input.txt", encoding="UTF-8")
numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
           "six": 6, "seven": 7, "eight": 8, "nine": 9}
result = 0
for line in f:
    for key in numbers:
        index = line.find(key)
        if index != -1:
            line = line[:index+1]+str(numbers[key]) + line[index+1:]
        index = line.rfind(key)
        if index != -1:
            line = line[:index+1]+str(numbers[key]) + line[index+1:]
    digitsAll = re.findall(r'\d', line)
    result += int(str(digitsAll[0]) + str(digitsAll[-1]))

print(result)
