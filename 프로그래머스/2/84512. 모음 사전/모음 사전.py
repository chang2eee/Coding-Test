from itertools import product

def solution(word):
    answer = 0
    dictionary = []
    
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    for i in range(1, 6):
        temp = product(vowels, repeat=i)
        for element in temp:
            dictionary.append(''.join(element))
    
    dictionary.sort()
    
    answer = dictionary.index(word)+1
    
    return answer