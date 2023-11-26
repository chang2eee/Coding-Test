def solution(myString, pat):
    answer = 0
    temp = ''
    
    for string in myString:
        if string == 'A':
            temp += 'B'
        elif string == 'B':
            temp += 'A'
            
    if pat in temp:
        answer = 1
    
    return answer