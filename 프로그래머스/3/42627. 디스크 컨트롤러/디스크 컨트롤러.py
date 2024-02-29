from heapq import *

def solution(jobs):
    answer = 0
    
    now, count = 0, 0
    start = -1  # 시작 전 표시
    
    heap = []
    
    while count < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heappush(heap, (job[1], job[0]))
                
        if len(heap) > 0:
            execute_time, arrival_time = heappop(heap)
            
            start = now
            now += execute_time
            
            answer += now - arrival_time
            
            count += 1
        
        else:
            now += 1
            
    answer //= count
    
    return answer