
from math import prod

with open('input.txt', 'r') as inputFile:
    lines = [line.strip() for line in inputFile]

def part_one():
    opp = set()
    for line in lines:
        num = int(line)
        num2 = 2020 - num

        if num in opp:
            print(num * num2)
            return
        else:
            opp.add(num2)

def part_two():
    singles = {}
    pairs = {}
    for line in lines:
        num = int(line)
        
        for pair in pairs:
            if 2020 == int(pair) + num:
                print(prod(pairs[pair]) * num)
                return

        for single in singles:
            s = singles[single] + num 
            if s < 2020:
                pairs[s] = (singles[single], num)        

        singles[num] = num

part_one()
part_two()