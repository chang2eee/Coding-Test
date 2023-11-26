def solution(myString):
    answer = ''
    target = 'abcdefghijk'
    
    for element in myString:
        if element in target:
            answer += 'l'
        else:
            answer += element
    
    
    return answer