import math
import time
from functools import reduce

with open('test.txt', 'r') as inputFile:
    lines = [line.strip() for line in inputFile]

def part_one():
    earliest = int(lines[0])
    buses = [int(bus) for bus in lines[1].split(',') if not bus == 'x']

    min_d = 999
    min_bus = 0
    for bus in buses:
        d = math.ceil(earliest / bus) * bus - earliest
        if d < min_d:
            min_d = d
            min_bus = bus
    print(min_d * min_bus)

    pass

# copied
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def part_two():
    start = time.time()
    buses = [(i, int(bus)) for i, bus in enumerate(lines[1].split(',')) if not bus == 'x']
    times = []
    remainders = []
    for (i, bus) in buses:
        times.append(bus)
        remainders.append((-i)%bus)
        print(i, bus, (-i)%bus)

    print(chinese_remainder(times, remainders))


part_one()
part_two()
