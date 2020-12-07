with open('input.txt', 'r') as inputFile:
    forest = [list(line) for line in inputFile]
frows = len(forest)
fcols = len(forest[0])

def step_fwd(row, col, row_inc, col_inc):
    return (row + row_inc, col + col_inc)

def get_cell(row, col):
    return forest[row][col%(fcols-1)]

def check_trees(row_inc, col_inc):
    row = 0
    col = 0
    tree_count = 0
    while row < frows:
        if get_cell(row, col) == "#":
            tree_count += 1
        row, col = step_fwd(row, col, row_inc, col_inc)
    return tree_count

def part_one():
    print(check_trees(1, 3))

def part_two():
    print(check_trees(1, 1) * check_trees(1, 3) * check_trees(1, 5) * check_trees(1, 7) * check_trees(2, 1))

part_one()
part_two()
