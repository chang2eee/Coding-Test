def solution(binomial):
    elements = binomial.split()
    
    a = int(elements[0])
    b = int(elements[2])
    op = str(elements[1])

    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    else:
        result = None

    return result

