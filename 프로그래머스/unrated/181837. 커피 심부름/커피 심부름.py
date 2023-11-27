def solution(order):
    answer = 0
    
    for element in order:
        if 'americano' in element or 'anything' in element:
            answer += 4500
        else:
            answer += 5000
    
    return answer