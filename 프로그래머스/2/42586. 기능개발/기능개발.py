from math import ceil

def solution(progresses, speeds):
    answer = []
    
    remain = []
    
    for progress in progresses:
        remain.append(100 - progress)
    
    temp = []
    
    for r, s in zip(remain, speeds):
        temp.append(ceil(r / s))
    
    stack = []
    
    for element in temp:
        if not stack:
            stack.append(element)
        else:
            if max(stack) >= element:
                stack.append(element)
            else:
                answer.append(len(stack))
                stack.clear()
                stack.append(element)
    
    if stack:
        answer.append(len(stack))
    
    return answer