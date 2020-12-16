with open('input.txt', 'r') as inputFile:
    lines = [line.strip() for line in inputFile]

def move(shift, input):
    return input + eval(shift)

def step(op, shift, index, val):
    if op == 'nop':
        return index + 1, val
    elif op == 'acc':
        return index + 1, move(shift, val)
    elif op == 'jmp':
        return move(shift, index), val

def test_program(program, index, val):
    instructions = set()
    while True:
        if index in instructions:
            return False, val
        instructions.add(index)
        try:
            action = program[index]
        except IndexError:
            return True, val
        (op, shift) = action.split(" ")
        index, val = step(op, shift, index, val)

    return True, val

def part_one():
    (success, val) = test_program(lines, 0, 0)
    return val

def part_two():
    success = False

    for i, line in enumerate(lines):
        if 'nop' in line:
            lines[i] = line.replace('nop', 'jmp')
            (success, val) = test_program(lines, 0, 0)
            if success:
                return val
            lines[i] = line.replace('jmp', 'nop')
        elif 'jmp' in line:
            lines[i] = line.replace('jmp', 'nop')
            (success, val) = test_program(lines, 0, 0)
            if success:
                return val
            lines[i] = line.replace('nop', 'jmp')
        else:
            continue
    


print(part_one())
print(part_two())
