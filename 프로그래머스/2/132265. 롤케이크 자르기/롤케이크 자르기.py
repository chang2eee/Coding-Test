from collections import Counter

def solution(topping):
    answer = 0
    topping_counter = Counter(topping)
    left = set()
    
    for element in topping:
        topping_counter[element] -= 1
        left.add(element)
        
        if topping_counter[element] == 0:
            topping_counter.pop(element)
            
        if len(topping_counter) == len(left):
            answer += 1
    
    
    return answer