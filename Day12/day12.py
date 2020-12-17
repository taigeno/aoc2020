with open('input.txt', 'r') as inputFile:
    lines = [line.strip() for line in inputFile]

def parse_line(line):
    return line[0], int(line[1:])

def part_one():
    face = 0 # E = 0, 1 = N, 2 = W, 3 = S
    north = 0
    east = 0

    for line in lines:
        action, value = parse_line(line)
        if action == 'N':
            north += value
        elif action == 'S':
            north -= value
        elif action == 'E':
            east += value
        elif action == 'W':
            east -= value
        elif action == 'R':
            face = (face - value/90 + 4)%4
        elif action == 'L':
            face = (face + value/90)%4
        elif action == 'F':
            if face == 0:
                east += value
            elif face == 1:
                north += value
            elif face == 2:
                east -= value
            elif face == 3:
                north -= value

    print(abs(north) + abs(east))

def rotate(waypoint, value, direction):
    if value == 90:
        return direction * -waypoint[1], direction * waypoint[0]

    elif value == 180:
        return -waypoint[0], -waypoint[1]

    elif value == 270:
        return direction * waypoint[1], direction * -waypoint[0]

def part_two():
    waypoint = [10, 1] # E / N
    north = 0
    east = 0

    for line in lines:
        action, value = parse_line(line)
        if action == 'N':
            waypoint[1] += value
        elif action == 'S':
            waypoint[1] -= value
        elif action == 'E':
            waypoint[0] += value
        elif action == 'W':
            waypoint[0] -= value
        elif action == 'R':
            waypoint[0], waypoint[1] = rotate(waypoint, value, -1)
            #face = (face - value/90 + 4)%4
            pass
        elif action == 'L':
            waypoint[0], waypoint[1] = rotate(waypoint, value, 1)
            pass
        elif action == 'F':
            east += value * waypoint[0]
            north += value * waypoint[1]

    print(abs(north) + abs(east))

part_one()
part_two()