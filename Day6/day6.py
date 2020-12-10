with open('input.txt', 'r') as inputFile:
    lines = [line.strip() for line in inputFile]

def part_one():
    answers = set()
    s = 0
    groups = []
    for line in lines:
        if line == '':
            s += len(set.union(*groups))
            groups = []
        else:
            groups.append(set(line))
    s += len(set.union(*groups))
    print(s)

def part_two():
    s = 0
    groups = []
    for line in lines:
        if line == '':
            s += len(set.intersection(*groups))
            groups = []
        else:
            groups.append(set(line))
    s += len(set.intersection(*groups))
    print(s)

part_one()
part_two()
