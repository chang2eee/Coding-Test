from heapq import *

def solution(scoville, K):
    answer = 0
    scoville.sort()
    
    while scoville[0] < K and len(scoville) > 1:
        small = heappop(scoville)
        big = heappop(scoville)
        
        new = small + 2 * big
        
        heappush(scoville, new)       
        
        answer += 1
    
    if scoville[0] >= K:
        return answer
    else:
        return -1