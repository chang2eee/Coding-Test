from itertools import combinations

def solution(nums):
    answer = 0

    temp = list(combinations(nums, 3))
    
    numbers = []
    
    for element in temp:
        numbers.append(sum(element))
    
    for number in numbers:
        if check(number) == True:
            answer += 1
    
    return answer

def check(number):
    result = 0
    
    for i in range(2, number + 1):
        if number % i == 0:
            result += 1
    
    if result == 1:
        return True
    else:
        return False