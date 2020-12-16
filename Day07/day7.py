import re

with open('input.txt', 'r') as inputFile:
    lines = [line.strip() for line in inputFile]

def get_keys():
    for line in lines:
        tokens = re.split(r" bags contain ", line)
        container = tokens[0]
        containees = re.findall(r'(?<=\d )[a-z ]+(?= bag)', tokens[1])
        yield container, containees

bags = { key: value for (key, value) in get_keys() }

def has_gold(bag):
    if bag == 'shiny gold':
        return False
    elif len(bags[bag]) == 0:
        return False
    elif 'shiny gold' in bags[bag]:
        return True
    else:
        return any([has_gold(item) for item in bags[bag]])

def part_one():
    print(sum([has_gold(item) == True for item in bags]))
    pass

def get_nkeys():
    for line in lines:
        tokens = re.split(r" bags contain ", line)
        container = tokens[0]
        containees = re.findall(r'[0-9]+[a-z ]+(?= bag)', tokens[1])
        yield container, containees

nbags = { key: value for (key, value) in get_nkeys() }

def num_bags(bag):
    num = re.search(r"[0-9]+", bag)
    bag = re.search(r"[a-z][a-z ]+", bag).group(0)
    count = 1
    if num != None:
        count = int(num.group(0))
    
    if len(nbags[bag]) == 0:
        return 1 * count
    else:
        return sum([num_bags(item) for item in nbags[bag]]) * count + count

def part_two():
    print(num_bags('shiny gold') - 1)

part_one()
part_two()
