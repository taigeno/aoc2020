import copy
from collections import Counter
import time

with open('input.txt', 'r') as inputFile:
    layout = [list(line.strip()) for line in inputFile]
    nrow = len(layout)
    ncol = len(layout[0])

offsets = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1]
]

def count_neighbors(row, col, grid, extended):
    total = 0
    for off in offsets:
        row_x = row + off[0]
        col_x = col + off[1]
        while True:
            if row_x < 0 or col_x < 0 or row_x >= nrow or col_x >= ncol:
                break

            if grid[row_x][col_x] == '#':
                total += 1
                break
            elif grid[row_x][col_x] == 'L':
                break
            elif not extended:
                break
                
            row_x += off[0]
            col_x += off[1]

    return total

def one_round(grid, extended):
    max_neigh = 5 if extended else 4
    retGrid = copy.deepcopy(grid)
    changed = False
    for i, row in enumerate(grid):
        for j, column in enumerate(row):
            curr_cell = grid[i][j]
            if curr_cell == 'L' or curr_cell == '#':
                neighbors = count_neighbors(i, j, grid, extended)

                if curr_cell == 'L' and neighbors == 0:
                    changed = True
                    retGrid[i][j] = '#'
                elif curr_cell == '#' and neighbors >= max_neigh:
                    changed = True
                    retGrid[i][j] = 'L'

    return retGrid, changed

def run_sym(extended):
    grid = copy.deepcopy(layout)
    changed = True
    while changed:
        grid, changed = one_round(grid, extended)

    items = Counter(item for row in grid for item in row)
    print(items['#'])

def part_one():
    start = time.time()
    run_sym(False)
    end = time.time()
    print(end - start)
    
def part_two():
    start = time.time()
    run_sym(True)
    end = time.time()
    print(end - start)

part_one()
part_two()
