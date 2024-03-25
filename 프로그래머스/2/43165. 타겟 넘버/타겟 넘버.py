def solution(numbers, target):
    answer = 0
    
    def dfs(numbers, target, idx, current):
        nonlocal answer
        
        if idx == len(numbers):
            if current == target:
                answer += 1
            return 
        
        dfs(numbers, target, idx+1, current-numbers[idx])
        dfs(numbers, target, idx+1, current+numbers[idx])

    dfs(numbers, target, 0, 0)
    return answer
