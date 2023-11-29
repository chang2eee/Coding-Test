def solution(arr):
    answer = []
    
    target = min(arr)
    
    arr.remove(target)
    
    if not arr:
        arr.append(-1)
    
    return arr