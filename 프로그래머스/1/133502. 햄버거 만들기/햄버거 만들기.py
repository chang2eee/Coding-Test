def solution(ingredient):
    answer = 0
    
    stack = []
    
    for element in ingredient:
        stack.append(element)
        
        if stack[-4:] == [1, 2, 3, 1]:
            answer += 1
            
            for k in range(4):
                stack.pop()
    
    return answer