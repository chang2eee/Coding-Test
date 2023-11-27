def solution(s):
    answer = 0
    stack = []
    
    s = s.split(' ')
    
    for element in s:
        if element == 'Z':
            stack.pop()
        else:
            stack.append(int(element))
    
    answer = sum(stack)
    
    return answer