answer = 0

def solution(numbers, target):
    global answer
    
    dfs(numbers, target, 0, 0)
    
    return answer

def dfs(numbers, target, index, current_value):
    global answer
    
    if index == len(numbers):
        if current_value == target:
            answer += 1
        return
    else:
        dfs(numbers, target, index+1, current_value - numbers[index])
        dfs(numbers, target, index+1, current_value + numbers[index])