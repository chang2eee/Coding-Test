from itertools import permutations

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    container = set([int(n) for n in numbers])
    
    for i in range(2, len(numbers)+1):
        temp = list(permutations(numbers, i))
        for element in temp:
            number = ''.join(element)
            container.add(int(number))
    print(container)
    
    for element in container:
        if check(element):
            print(element)
            answer += 1
    
    return answer

from math import sqrt

def check(number):
    if number <= 1:
        return False
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True