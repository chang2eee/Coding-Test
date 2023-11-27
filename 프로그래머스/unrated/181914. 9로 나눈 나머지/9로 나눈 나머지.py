def solution(number):
    answer = 0
    temp = 0
    
    for num in number:
        temp += int(num)
        
    answer = temp % 9
    return answer