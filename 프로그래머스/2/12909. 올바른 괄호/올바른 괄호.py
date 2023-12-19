def solution(s):
    answer = True
    stack = []
    
    for element in s:
        if not stack:
            stack.append(element)
        else:
            if element == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(element)
            else:
                stack.append(element)
    
    if stack:
        answer = False
    
    
    return answer