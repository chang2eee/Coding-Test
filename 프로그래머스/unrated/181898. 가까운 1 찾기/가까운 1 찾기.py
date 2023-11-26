def solution(arr, idx):
    answer = -1
    
    for i in range(len(arr)):
        if i < idx:
            continue
        else:
            if arr[i] != 1:
                continue
            else:
                answer = i
                break
            
    
    return answer