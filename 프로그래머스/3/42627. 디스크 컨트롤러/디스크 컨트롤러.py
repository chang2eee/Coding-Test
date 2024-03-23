from heapq import *

def solution(jobs):
    answer = 0
    
    now, count = 0, 0
    start = -1
    
    heap = []
    
    while count < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heappush(heap, (job[1], job[0]))
        
        if len(heap) > 0:
            run_time, arrival_time = heappop(heap)
            
            start = now
            now += run_time
            answer += (now - arrival_time)
            count += 1
        else:
            now += 1
    return answer // count