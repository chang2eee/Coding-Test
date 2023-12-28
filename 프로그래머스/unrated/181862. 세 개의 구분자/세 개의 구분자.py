def solution(myStr):
    answer = []
    
    splitter = ['a', 'b', 'c']
    temp = ''
    
    for element in myStr:
        if element in splitter:
            if temp:
                answer.append(temp)
                temp = ''
        else:
            temp += element
    
    if temp:
        answer.append(temp)
    
    if not answer:
        answer.append('EMPTY')
        
    return answer