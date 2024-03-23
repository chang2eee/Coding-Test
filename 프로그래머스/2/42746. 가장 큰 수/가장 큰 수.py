def solution(numbers):
    answer = ''
    
    numbers = [str(number) for number in numbers]
    numbers.sort(key=lambda x:x*10, reverse=True)
    
    for n in numbers:
        answer += n
    
    
    
    return str(int(answer))