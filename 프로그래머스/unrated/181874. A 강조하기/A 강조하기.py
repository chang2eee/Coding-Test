def solution(myString):
    answer = ''
    
    myString = myString.lower()
    
    for string in myString:
        if string == 'a':
            answer += string.upper()
        else:
            answer += string
    return answer