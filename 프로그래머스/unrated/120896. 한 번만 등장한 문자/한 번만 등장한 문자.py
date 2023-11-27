from collections import Counter

def solution(s):
    answer = ''
    
    counter = Counter(list(s))
    
    for element in s:
        if counter[element] < 2:
            answer += element
    
    answer = ''.join(sorted(answer))
    
    return answer