answer = [0, 0]

def solution(arr):
    global answer
    N = len(arr)
    
    compare(arr, 0, 0, N)
    
    
    
    return answer

def compare(arr, x, y, n):
    global answer
    init = arr[x][y]
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != init:
                next_n = n // 2
                
                compare(arr, x, y, next_n)
                compare(arr, x+next_n, y, next_n)
                compare(arr, x, y+next_n, next_n)
                compare(arr, x+next_n, y+next_n, next_n)
                
                return 
    answer[init] += 1