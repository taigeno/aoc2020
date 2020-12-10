
from math import prod
from itertools import combinations

with open('input.txt', 'r') as inputFile:
    lines = [line.strip() for line in inputFile]


def get_sum(num):
    for comb in combinations(lines, num):
        if sum(comb) == 2020:
            print(prod(comb))    

def part_one():
    get_sum(2)

def part_two():
    get_sum(3)

part_one()
part_two()