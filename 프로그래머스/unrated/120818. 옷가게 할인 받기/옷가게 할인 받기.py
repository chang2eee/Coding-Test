def solution(price):
    answer = 0
    
    if 0 < price < 100000:
        answer = price
    elif 100000<= price < 300000:
        answer = price * 0.95
    elif 300000<= price < 500000:
        answer = price * 0.90
    else:
        answer = price * 0.80
        
    
    return int(answer)