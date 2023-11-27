def solution(my_string):
    answer = []
    
    dic = dict()
    
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_lower = alphabet_upper.lower()
    
    for element in alphabet_upper:
        dic[element] = 0
    for element in alphabet_lower:
        dic[element] = 0
        
    for element in my_string:
        dic[element] += 1
    
    for value in dic.values():
        answer.append(value)
    
    
    return answer