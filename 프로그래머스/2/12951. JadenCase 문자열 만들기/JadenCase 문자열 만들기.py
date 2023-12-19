def solution(s):
    answer = ''
    
    s = s.split(' ')
    
    for element in s:
        for i in range(len(element)):
            if i == 0:
                if element[i].isdigit():
                    answer += element[i]
                elif element[i].isalpha():
                    answer += element[i].upper()
            else:   # i != 0:
                answer += element[i].lower()
        answer += ' '
    
    answer = answer[:-1]
    
    return answer