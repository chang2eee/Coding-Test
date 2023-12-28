from collections import deque

def solution(s):
    answer = 0
    
    s = deque(s)
    
    for i in range(len(s)):
        answer += check(s)
        s.rotate(1)
    
    return answer

def check(s):
    result = 1
    
    stack = []
    
    for element in s:
        if not stack:
            stack.append(element)
        else:
            if stack[-1] == '(' and element == ')':
                stack.pop()
            elif stack[-1] == '{' and element == '}':
                stack.pop()
            elif stack[-1] == '[' and element == ']':
                stack.pop()
            else:
                stack.append(element)
            
    if not stack:
        return result
    else:
        return 0           