def solution(s):
    answer = ''
    
    s = s.split(' ')
    
    for element in s:
        for i in range(len(element)):
            if i % 2 == 0:
                answer += element[i].upper()
            else:
                answer += element[i].lower()
        
        answer += ' '
    
    answer = answer[:len(answer)-1]
    
    return answer