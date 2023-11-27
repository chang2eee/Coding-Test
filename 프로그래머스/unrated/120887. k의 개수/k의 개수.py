def solution(i, j, k):
    answer = 0
    temp = []
    
    for number in range(i, j+1):
        temp.append(str(number))    
    
    for element in temp:
        answer += element.count(str(k))
    
    return answer