answer = 0

def solution(numbers, target):
    global answer
    
    dfs(0, numbers, target, 0)
    
    return answer

def dfs(idx, numbers, target, value):
    global answer
    
    if idx == len(numbers):
        if value == target:
            answer += 1
            return 
        else:
            return 
    
    else:
        dfs(idx+1, numbers, target, value + numbers[idx])
        dfs(idx+1, numbers, target, value - numbers[idx])