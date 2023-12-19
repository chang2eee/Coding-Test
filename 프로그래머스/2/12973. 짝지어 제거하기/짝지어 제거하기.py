def solution(s):
    answer = 0
    
    stack = []
    
    for element in s:
        if not stack:
            stack.append(element)
        else:
            if element == stack[-1]:
                stack.pop()
            else:
                stack.append(element)
    
    if not stack:
        answer = 1

    

    return answer