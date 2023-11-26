def solution(myString):
    myString = myString.split('x')
    
    answer = []
    
    for element in myString:
        if element.isalpha():
            answer.append(element)
    
    answer.sort()
    
    return answer