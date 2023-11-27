def solution(arr):
    answer = []
    stk = []
    
    i = 0
    length = len(arr)
    
    while i < length:
        if not stk:
            stk.append(arr[i])
            i += 1
        elif stk[-1] == arr[i]:
            stk.pop()
            i += 1
        elif stk[-1] != arr[i]:
            stk.append(arr[i])
            i += 1
    
    if stk:
        answer = stk.copy()
    else:
        answer = [-1]
    
    return answer