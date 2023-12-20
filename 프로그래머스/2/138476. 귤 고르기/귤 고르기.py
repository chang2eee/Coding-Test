from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    tangerine_counter = Counter(tangerine)
    
    tangerine_counter = sorted(tangerine_counter.items(), key=lambda x:x[1], reverse=True)
    
    for key, value in tangerine_counter:
        if k <= 0:
            break
        else:
            k -= value
            answer += 1
    
    return answer