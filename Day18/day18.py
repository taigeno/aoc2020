

with open('input.txt', 'r') as inputFile:
    lines = [line.strip().replace(" ", "") for line in inputFile]

def do_math(postfix):
    stack = []
    for i in postfix:
        if type(i) is int:
            stack.append(i)
            continue

        op1, op2 = stack.pop(), stack.pop()
        
        if i == '+':
            stack.append(op1 + op2)
        elif i == '*':
            stack.append(op1 * op2)
        
    return stack.pop()

def is_number(item):
    try:
        int(item)
        return True
    except ValueError:
        return False

def peek(stack):
    return stack[-1] if stack else None

def greater_precedence(op1, op2, precedences):
    return precedences[op1] >= precedences[op2]

def left_associative(op):
    return True

def make_eq(eq, precedences):
    out_stack = []
    op_stack = []
    for item in eq:
        if is_number(item):
            out_stack.append(int(item))
        elif item == '(':
            op_stack.append(item)
        elif item == ')':
            top = peek(op_stack)
            while top != '(':
                out_stack.append(op_stack.pop())
                top = peek(op_stack)
            op_stack.pop()
        else:
            top = peek(op_stack)
            while ((top is not None and top not in "()") 
                and greater_precedence(top, item, precedences) and left_associative(item)):
                out_stack.append(op_stack.pop())
                top = peek(op_stack)
            op_stack.append(item)
    while len(op_stack) != 0:
        out_stack.append(op_stack.pop())

    return out_stack

def part_one():
    precedences = {'+': 0, '*': 0}
    total = 0
    for line in lines:
        postfix = make_eq(line, precedences)
        total += do_math(postfix)

    print(total)
        
    pass

def part_two():
    precedence = {'+': 1, '*': 0}
    total = 0
    for line in lines:
        postfix = make_eq(line, precedence)
        total += do_math(postfix)

    print(total)
        

part_one()
part_two()