# Card   1: 58 68  1 21 88 37 66 61 23 25 | 63 95 45 43 79 64 29 87  8 70 84 34 91 67  3 76 27 24 28 62 13 54 19 93  7
import collections

f = open("/Users/alinasafina/PycharmProjects/aoc2023/aoc_day_4/input.txt", encoding="UTF-8")
lines = list(f.read().split("\n"))
result = 0
dictOfCards = {}
total = 0
totalRows = []
for index, line in enumerate(lines):
    line = line.split(":")[1].split("|")
    win_num = list(map(int, line[0].split()))
    reg_num = list(map(int, line[1].split()))
    counter = 0
    for i in reg_num:
        if i in win_num:
            counter += 1
    #         уходит в бесконечный цикл
    # for i in range(index+1, index+counter+1):
    #     print(1)
    #     lines.insert(i, lines[i])



print(len(lines))

# нужно разобраться
# def process_card_2(card: str):
#     card_id = int(card[:card.index(':')].split()[-1])
#     winning_numbers = card[card.index(':')+1:card.index('|')-1].split()
#     my_numbers = card[card.index('|')+1:].strip().split()
#     count = 0
#     for e in my_numbers:
#         if e in winning_numbers:
#             count += 1
#     return card_id, count
#
# file_dict = {}
# max_value = 0
# for line in lines:
#     id, winnings = process_card_2(line)
#     if winnings > max_value:
#         max_value = winnings
#     file_dict[id] = [winnings, 1]
# for i in range(len(file_dict) + 1, max_value + len(file_dict)):
#     file_dict[i] = [0, 0, 0]
#
# for id in file_dict.keys():
#     for e in range(file_dict[id][1]):
#         for i in range(file_dict[id][0]):
#             file_dict[id + i + 1][1] += 1
#
# total_winning_cards = 0
# for val in file_dict.values():
#     if len(val) == 2:
#         total_winning_cards += val[1]
# print(total_winning_cards)
