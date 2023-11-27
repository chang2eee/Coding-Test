def solution(emergency):
    answer = []
    dic = dict()
    temp = []

    for element in emergency:
        temp.append(element)
        
    temp.sort(reverse=True)
    
    for idx, value in enumerate(temp):
        dic[value] = idx + 1
    
    
    for element in emergency:
        answer.append(dic[element])
    
    return answer