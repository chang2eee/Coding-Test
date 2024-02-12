from heapq import *

def solution(n, k, enemy):
    answer = 0
    
    sum_value = 0
    heap = []
    
    for e in enemy:
        heappush(heap, -e)
        
        sum_value += e
        
        if sum_value > n:
            if k == 0:
                break
            sum_value += heappop(heap)
            
            k -= 1
        answer += 1
    
    
    
    return answer