# Card   1: 58 68  1 21 88 37 66 61 23 25 | 63 95 45 43 79 64 29 87  8 70 84 34 91 67  3 76 27 24 28 62 13 54 19 93  7

f = open("/Users/alinasafina/PycharmProjects/aoc2023/aoc_day_4/input.txt", encoding="UTF-8")
result = 0
for line in f:
    line = line.split(":")[1].split("|")
    win_num = list(map(int, line[0].split()))
    reg_num = list(map(int, line[1].split()))
    counter = 0
    for i in reg_num:
        if i in win_num:
            counter += 1
    if counter > 2:
        result += 2 ** (counter-1)
    elif counter == 1:
        result += 1
    elif counter == 2:
        result += 2

print(result)
