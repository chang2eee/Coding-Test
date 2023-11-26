def solution(n):
    answer = 0
    
    temp = []
    
    for i in range(1, 100):
        temp.append(6 * i)
    
    for element in temp:
        if element % 6 == 0 and element % n == 0:
            answer = element / 6
            break
    
    return answer