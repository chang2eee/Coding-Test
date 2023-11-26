def solution(numbers, direction):
    
    if direction == 'right':
        temp = numbers.pop(-1)
        numbers.insert(0, temp)
    else:
        temp = numbers.pop(0)
        numbers.append(temp)
    
    return numbers