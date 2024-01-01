# from collections import deque

# def solution(numbers):
#     answer = [-1] * len(numbers)
#     queue = deque(numbers)
    
#     idx = 0
    
#     while queue:
#         number = queue.popleft()
        
#         if not queue:
#             answer[idx] = -1
#         else:
#             for element in queue:
#                 if number < element:
#                     answer[idx] = element
#                     break
#                 else:
#                     continue
#         idx += 1
    
#     return answer

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for i, number in enumerate(numbers):
        while stack and number > numbers[stack[-1]]:
            top = stack.pop()
            answer[top] = number
        
        stack.append(i)
    
    return answer