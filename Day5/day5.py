from math import floor

with open('input.txt', 'r') as inputFile:
    lines = [line.strip() for line in inputFile]

def get_row(code):
    left = 0
    right = 127
    for char in code:
        half = (right - left + 1) / 2
        if char == 'F':
            right -= half
        else:
            left += half
    return left

def get_col(code):
    left = 0
    right = 7
    for char in code:
        half = (right - left + 1) / 2
        if char == 'R':
            left += half
        else:
            right -= half
    return left

def get_seatid(row_code, col_code):
    row = get_row(row_code)
    col = get_col(col_code)
    return row * 8 + col

def part_one():
    high = 0
    for line in lines:
        rowid = get_seatid(line[0:7], line[7:10])
        if rowid > high:
            high = rowid
    print(high)

def part_two():
    """
    sum of consecutive ints = (n / 2) * (high + low)
    Diff with total sum is the missing number
    """
    high = 0
    low = 1000000
    s = 0
    for line in lines:
        rowid = get_seatid(line[0:7], line [7:10])
        if rowid > high:
            high = rowid
        if rowid < low:
            low = rowid
        s += rowid
    n = high - low + 1
    r = (n / 2) * (high + low) - s
    print(r)

part_one()
part_two()
