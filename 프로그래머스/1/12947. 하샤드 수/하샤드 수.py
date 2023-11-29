def solution(x):
    answer = True
    
    temp = str(x)
    temp_sum = 0
    
    for element in temp:
        temp_sum += int(element)    
        
    if x % temp_sum != 0:
        answer = False
    
    return answer