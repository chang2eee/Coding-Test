def solution(myStr):
    answer = []
    target = ['a', 'b', 'c']
    temp = ''

    for element in myStr:
        if element not in target:
            temp += element
        else:
            if temp:  
                answer.append(temp)
                temp = ''

    if temp:
        answer.append(temp)
        
    if len(answer) == 0:
        answer = ["EMPTY"]

    return answer
