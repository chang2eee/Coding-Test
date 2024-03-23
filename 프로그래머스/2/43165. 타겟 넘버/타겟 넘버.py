answer = 0

def dfs(numbers, target, index, current):
    global answer
    
    if index == len(numbers):
        if current == target:
            answer += 1
        return 
    
    dfs(numbers, target, index+1, current-numbers[index])
    dfs(numbers, target, index+1, current+numbers[index])

def solution(numbers, target):
    global answer
    
    dfs(numbers, target, 0, 0)
    return answer