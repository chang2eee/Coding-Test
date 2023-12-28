from itertools import product

def solution(word):
    answer = 0
    
    result = []
    
    alphabet = ['A', 'E', 'I', 'O', 'U']
    
    for i in range(1, 6):
        temp = product(alphabet, repeat = i)    
        for element in temp:
            result.append(''.join(element))
    
    result.sort()
    
    answer = result.index(word) + 1
    
    return answer