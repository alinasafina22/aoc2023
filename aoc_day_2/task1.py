# 12 red cubes, 13 green cubes,
# and 14 blue cubes. What is the sum of the IDs of those games?
# Game 3: 10 blue, 3 green, 8 red; 15 green, 14 blue, 1 red; 8 blue, 11 red, 2 green; 5 red, 9 green, 6 blue
import re

f = open("/Users/alinasafina/PycharmProjects/aoc2023/aoc_day_2/input.txt", encoding="UTF-8")
result = 0
for line in f:
    game = line.split(":")
    gameNumber = int(re.findall(r'\b\d+\b', game[0])[0])
    gameCubes = game[1].split(";")
    flag = True
    for i in gameCubes:
        for j in i.split(","):
            if int(j.split()[0]) > {'red': 12, 'green': 13, 'blue': 14}.get(j.split()[1], 0):
                flag = False
    if flag:
        result += gameNumber
print(result)
