from heapq import *

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    
    while scoville[0] < K and len(scoville) >= 2:
        small = heappop(scoville)
        big = heappop(scoville)
        
        heappush(scoville, 2*big+small)
        
        answer += 1
    
    if scoville[0] < K:
        return -1
    
    return answer