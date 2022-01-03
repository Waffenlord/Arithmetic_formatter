def arithmetic_arranger(operations, solution = False):
    if len(operations) > 5:
        print('Error: Too many problems')

    elif len(operations) == 1:
        error = check_errors(operations[0])
        if error:
            print(error)
        else:
            operation1 = operations[0].split()
            largest = max(operation1, key= lambda x: len(x))
            row1, row2, row3 = formating_operation(largest, operation1)
            print(row1)
            print(row2)
            print(row3)
            if solution:
                r = show_solution(operation1)
                space_number_row4 = len(largest) + 2 - len(r)
                row4 = ' ' * space_number_row4 + r
                print(row4)

    elif len(operations) == 2:
        error = check_errors(operations[0], operations[1])
        if error:
            print(error)
        else:
            l_row1, l_row2, l_row3, l_row4 = two_or_more(operations)
            print(l_row1[0] + '    ' + l_row1[1])
            print(l_row2[0] + '    ' + l_row2[1])
            print(l_row3[0] + '    ' + l_row3[1])
            if solution:
                print(l_row4[0] + '    ' + l_row4[1])



    elif len(operations) == 3:
        error = check_errors(operations[0], operations[1], operations[2])
        if error:
            print(error)
        else:
            l_row1, l_row2, l_row3, l_row4 = two_or_more(operations)
            print(l_row1[0] + '    ' + l_row1[1] + '    ' + l_row1[2])
            print(l_row2[0] + '    ' + l_row2[1] + '    ' + l_row2[2])
            print(l_row3[0] + '    ' + l_row3[1] + '    ' + l_row3[2])
            if solution:
                print(l_row4[0] + '    ' + l_row4[1] + '    ' + l_row4[2])
    
    elif len(operations) == 4:
        error = check_errors(operations[0], operations[1], operations[2], operations[3])
        if error:
            print(error)
        else:
            l_row1, l_row2, l_row3, l_row4 = two_or_more(operations)
            print(l_row1[0] + '    ' + l_row1[1] + '    ' + l_row1[2] + '    ' + l_row1[3])
            print(l_row2[0] + '    ' + l_row2[1] + '    ' + l_row2[2] + '    ' + l_row2[3])
            print(l_row3[0] + '    ' + l_row3[1] + '    ' + l_row3[2] + '    ' + l_row3[3])
            if solution:
                print(l_row4[0] + '    ' + l_row4[1] + '    ' + l_row4[2] + '   ' + l_row4[3])
    
    elif len(operations) == 5:
        error = check_errors(operations[0], operations[1], operations[2], operations[3], operations[4])
        if error:
            print(error)
        else:
            l_row1, l_row2, l_row3, l_row4 = two_or_more(operations)
            print(l_row1[0] + '    ' + l_row1[1] + '    ' + l_row1[2] + '    ' + l_row1[3] + '    ' + l_row1[4])
            print(l_row2[0] + '    ' + l_row2[1] + '    ' + l_row2[2] + '    ' + l_row2[3] + '    ' + l_row2[4])
            print(l_row3[0] + '    ' + l_row3[1] + '    ' + l_row3[2] + '    ' + l_row3[3] + '    ' + l_row3[4])
            if solution:
                print(l_row4[0] + '    ' + l_row4[1] + '    ' + l_row4[2] + '    ' + l_row4[3] + '    ' + l_row4[4])
                



def check_errors(*args):
    for x in args:
        l = x.split()
        if l[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        elif not l[0].isdigit() or not l[2].isdigit():
            return "Error: Numbers must only contain digits."
        elif len(l[0]) > 4 or len(l[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
    
    return False

def formating_operation(largest, l):
    space_number_row1 = len(largest) + 2 - len(l[0])
    row1 = ' ' * space_number_row1 + l[0]
    space_number_row2 = len(largest) + 1 - len(l[2])
    row2 = l[1] + ' ' * space_number_row2 + l[2]
    row3 = '-' * (len(largest) + 2)

    return row1, row2, row3

def show_solution(l):
    if l[1] == '+':
        result = int(l[0]) + int(l[2])
        return str(result)
    else:
        result = int(l[0]) - int(l[2])
        return str(result)

def two_or_more(operations):
    l_row1 = list()
    l_row2 = list()
    l_row3 = list()
    l_row4 = list()
    for op in operations:
        operation = op.split()
        largest = max(operation, key= lambda x: len(x))
        row1, row2, row3 = formating_operation(largest, operation)
        r = show_solution(operation)
        space_last_row = len(largest) + 2 - len(r)
        row4 = ' ' * space_last_row + r
        l_row1.append(row1)
        l_row2.append(row2)
        l_row3.append(row3)
        l_row4.append(row4)
    return l_row1, l_row2, l_row3, l_row4


arithmetic_arranger(['987 + 12', '56 + 289'], True)








