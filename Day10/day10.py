with open('input.txt', 'r') as inputFile:
    lines = [int(line.strip()) for line in inputFile]

def joltage(input):
    jolt = 0
    one_diff = 0
    three_diff = 0
    for i in input:
        if i - jolt == 1:
            one_diff += 1
        else:
            three_diff += 1
        jolt = i
    return one_diff * (three_diff + 1)

# How do you generalize this?
def get_combo(streak):
    if streak == 1:
        return 1
    if streak == 2:
        return 1
    if streak == 3:
        return 2
    if streak == 4:
        return 4
    if streak == 5:
        return 7
    return None

def combinations(input):
    streak = 1
    total = 1
    jolt = 0
    for i in input:
        if i - jolt == 1:
            streak += 1
        else:
            total *= get_combo(streak)
            streak = 1
        jolt = i
    total *= get_combo(streak)
    return total

def part_one():
    return joltage(sorted(lines))

def part_two():
    return combinations(sorted(lines))

print(part_one())
print(part_two())
