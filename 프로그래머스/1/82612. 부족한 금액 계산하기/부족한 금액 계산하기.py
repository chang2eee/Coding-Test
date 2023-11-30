def solution(price, money, count):
    answer = 0
    temp = []
    for i in range(1, count + 1):
        temp.append(price * i)
    
    answer = sum(temp) - money
    
    if answer <= 0:
        answer = 0

    return answer