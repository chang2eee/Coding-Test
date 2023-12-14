from math import sqrt

def solution(n):
    answer = 0
    
    for i in range(2, n+1):
        if check(i) == True:
            answer += 1
    
    return answer

def check(number):
    for i in range(2, int(sqrt(number))+1):
        if number % i == 0:
            return False
    return True