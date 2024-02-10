def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for i, number in enumerate(numbers):
        while stack and number > numbers[stack[-1]]:
            top = stack.pop()
            answer[top] = number
        
        stack.append(i)
    
    return answer