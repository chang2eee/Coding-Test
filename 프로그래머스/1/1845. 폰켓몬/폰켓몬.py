from collections import Counter

def solution(nums):
    answer = 0
    
    pokemon_counter = Counter(nums)
    take_amount = len(nums) // 2
    
    pokemon_kind = len(pokemon_counter.keys())
    
    if pokemon_kind > take_amount:
        answer = take_amount
    else:
        answer = pokemon_kind
    
    
    
    return answer