from math import sqrt

def solution(number, limit, power):
    answer = 0
    
    for element in range(1, number+1):
        count = getCount(element)
        if count <= limit:
            answer += count
        else:
            answer += power
    
    return answer

def getCount(number):
    result = 0
    
    sqrt_num = int(sqrt(number))
    for i in range(1, sqrt_num+1):
        if number % i == 0:
            result += 2  
    
    if sqrt_num**2 == number:
        result -= 1  
    
    return result
