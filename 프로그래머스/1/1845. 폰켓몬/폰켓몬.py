from collections import Counter

def solution(nums):
    answer = 0
    
    pokemon = Counter(nums)
    take = len(nums) // 2
    
    if take <= len(pokemon):
        return take
    else:
        return len(pokemon)
    
    return answer