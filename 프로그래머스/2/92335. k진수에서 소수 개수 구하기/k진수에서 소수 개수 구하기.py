import math

def solution(n, k):
    answer = 0
    
    temp_list = getNumber(n, k).split('0')
    print(temp_list)
    
    for element in temp_list:
        if not element or element == '1':
            continue
        elif check(int(element)):
            answer += 1
    
    return answer

def getNumber(n, k):
    temp = []
    
    while n != 0:
        temp.append(n % k)
        n //= k
        
    result = ''
    
    for idx in range(len(temp)-1, -1, -1):
        result += str(temp[idx])
    
    return result

def check(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:	
            return False
    return True