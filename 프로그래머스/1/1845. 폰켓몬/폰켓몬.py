from collections import Counter

def solution(nums):
    answer = 0
    
    pokemon = Counter(nums)
    
    pokemon_type, take_amount = len(pokemon), len(nums) // 2
    
    if take_amount <= pokemon_type:
        return take_amount
    else:
        return pokemon_type
    
    
    return answer