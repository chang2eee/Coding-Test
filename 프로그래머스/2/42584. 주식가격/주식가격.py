from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        current = prices.popleft()
        sec = 0
        
        for price in prices:
            sec += 1
            if current > price:
                break
        answer.append(sec)
                
    
    
    return answer