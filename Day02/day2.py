import re

with open('input.txt', 'r') as inputFile:
    lines = [line.strip() for line in inputFile]

def part_one():
    valid_count = 0
    for line in lines:
        (min_x, max_x, letter, text) = re.split('-|: | ', line)
        i = text.count(letter)
        if int(max_x) >= i & i >= int(min_x):
            valid_count += 1
    print(valid_count)

def part_two():
    valid_count = 0
    for line in lines:
        (pos_1, pos_2, letter, text) = re.split('-|: | ', line)

        if (text[int(pos_1) - 1] == letter) != (text[int(pos_2) - 1] == letter):
            valid_count += 1
    print(valid_count)

part_one()
part_two()
