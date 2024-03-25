def solution(n):
    answer = n
    
    n = bin(n)[2:]
    one_count = countOne(n)
    
    while True:
        answer += 1
        
        if one_count == countOne(bin(answer)[2:]):
            return answer
    
    return answer

def countOne(number):
    return number.count('1')