def solution(l, r):
    answer = []
    
    for number in range(l, r+1):
        if all(digit == '0' or digit == '5' for digit in str(number)):
            answer.append(number)
    
    return answer if answer else [-1]