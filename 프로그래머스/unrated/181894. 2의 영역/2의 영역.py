def solution(arr):
    answer = []
    
    start, end = -1, -1
    
    for i in range(len(arr)):
        if arr[i] == 2:
            start = i
            break
    
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == 2:
            end = i
            break
    
    answer = arr[start:end+1]
    
    if start == -1 and end == -1:
        answer = [-1]
    
    return answer