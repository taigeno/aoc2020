import re

with open('input.txt', 'r') as inputFile:
    lines = [line.strip() for line in inputFile]

def check_keys(keys):
    print(keys)
    if len(keys) == 8:
        return 1
    elif len(keys) == 7:
        if 'cid' not in keys:
            return 1
        else:
            return 0
    return 0

def part_one():
    keys = set()
    valid_count = 0
    for line in lines:
        if line == '':
            valid_count += check_keys(keys)
            keys.clear()
        else:
            items = re.split(r' ', line)
            for item in items:
                keys.add(item.split(":")[0])
    valid_count += check_keys(keys)
    print(valid_count)

def valid_key(kvpair):
    key = kvpair[0]
    value = kvpair[1]

    if key == 'byr':
        return 2002 >= int(value) >= 1920
    elif key == 'iyr':
        return 2020 >= int(value) >= 2010
    elif key == 'eyr':
        return 2030 >= int(value) >= 2020
    elif key == 'hgt':
        if 'cm' in value:
            val = int(value.split('c')[0])
            return 193 >= val >= 150
        elif 'in' in value:
            val = int(value.split('i')[0])
            return 76 >= val >= 59
        else:
            return False
    elif key == 'ecl':
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif key == 'hcl':
        return re.match(r'#[0-9a-f]{6}', value) != None
    elif key == 'pid':
        return re.match(r'^\d{9}$', value) != None

def part_two():
    keys = set()
    valid_count = 0
    for line in lines:
        if line == '':
            valid_count += check_keys(keys)
            keys.clear()
        else:
            items = re.split(r' ', line)
            for item in items:
                kvpair = item.split(":")
                if valid_key(kvpair):
                    keys.add(kvpair[0])
    valid_count += check_keys(keys)
    print(valid_count)
    pass

part_one()
part_two()
