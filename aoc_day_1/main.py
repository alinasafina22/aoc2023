f = open("/Users/alinasafina/PycharmProjects/pythonProject/aoc_day_1/input.txt", encoding="UTF-8")
dict1 = {"one": 1, "two": 2, "three": 3, "four": 4, "five" : 5,
         "six": 6, "seven": 7, "eight":8, "nine": 9}
result = 0
for line in f:
    firstDigit = ''
    secondDigit = ''
    indexOfFirstWord = 0
    indexOfSecondWord = 0
    indexOfFirstNumber = 0
    indexOfSecondNumber = 0
    for item, index in enumerate(line):
        if item.isdigit() and firstDigit == '':
            firstDigit = item
            indexOfFirstNumber = index
        elif item.isdigit() and firstDigit != '':
            secondDigit = item
            indexOfSecondNumber = index

    if secondDigit == '':
        result += int(firstDigit + firstDigit)
    else:
        result += int(firstDigit + secondDigit)
print(result)