from itertools import product

with open('input.txt', 'r') as inputFile:
    lines = [int(line.strip()) for line in inputFile]

def check_pairs(nums, target):
    for (a, b) in product(nums, repeat=2):
        if a + b == target:
            return True
    return False

def part_one():
    numbers = []
    preamble = 25
    for line in lines:
        if len(numbers) == preamble:
            if not check_pairs(numbers, line):
                return line
            numbers.pop(0)
        numbers.append(line)

def part_two(target):
    for i in range(len(lines)):
        sum = 0
        j = i
        while sum < target:
            sum += lines[j]
            if sum == target:
                return min(lines[i:j+1]) + max(lines[i:j+1])
            j += 1

t = part_one()
print(t)
print(part_two(t))
