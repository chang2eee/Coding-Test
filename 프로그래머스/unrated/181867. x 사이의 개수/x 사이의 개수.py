def solution(myString):
    answer = []
    
    myString = myString.split('x')
    
    for element in myString:
        answer.append(len(element))
    
    return answer