import time 

with open('input.txt', 'r') as inputFile:
    lines = [line.strip() for line in inputFile]

def get_turn(nums, num, turn):
    if num not in nums:
        return 0
    else:
        return turn - nums[num]

def run_game(line, nth):
    nums = {}
    last_num = -1
    turn = 0
    for num in line.split(','):
        if last_num != -1:
            nums[last_num] = turn
        turn += 1
        last_num = int(num)

    for i in range(turn, nth):
        # Get the new number
        num = get_turn(nums, last_num, i)
        # Add the previous number
        nums[last_num] = i
        last_num = num
    
    print(last_num)

def part_one():
    for line in lines:
        run_game(line, 2020)

def part_two():
    for line in lines:
        run_game(line, 30000000)

part_one()
part_two()
