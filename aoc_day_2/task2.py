import re

f = open("/Users/alinasafina/PycharmProjects/aoc2023/aoc_day_2/input.txt", encoding="UTF-8")
result = 0
for line in f:
    game = line.split(":")
    gameNumber = int(re.findall(r'\b\d+\b', game[0])[0])
    gameCubes = game[1].split(";")
    dictColors = {}
    multiColors = 1
    for i in gameCubes:
        for j in i.split(","):
            if j.split()[1] in dictColors:
                if dictColors.get(j.split()[1]) < int(j.split()[0]):
                    dictColors[j.split()[1]] = int(j.split()[0])
            else:
                dictColors[j.split()[1]] = int(j.split()[0])
    for i in dictColors:
        multiColors = multiColors * dictColors[i]
    result += multiColors
print(result)

