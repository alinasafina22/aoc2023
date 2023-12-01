f = open("/Users/alinasafina/PycharmProjects/aoc2023/aoc_day_1/input.txt", encoding="UTF-8")
dict1 = {"one": 1, "two": 2, "three": 3, "four": 4, "five" : 5,
         "six": 6, "seven": 7, "eight":8, "nine": 9}
result = 0
for line in f:
    firstDigit = ''
    secondDigit = ''
    for item in line:
        if item.isdigit() and firstDigit == '':
            firstDigit = item
        elif item.isdigit() and firstDigit != '':
            secondDigit = item

    if secondDigit == '':
        result += int(firstDigit + firstDigit)
    else:
        result += int(firstDigit + secondDigit)
print(result)