def solution(quiz):
    answer = []
    
    for element in quiz:
        element = element.split(' ')
        
        temp = ''
        
        for i in range(3):
            temp += str(element[i])
        
        if eval(temp) == int(element[-1]):
            answer.append('O')
        else:
            answer.append('X')
        
    
    
    return answer
