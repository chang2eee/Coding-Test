def solution(name, yearning, photo):
    answer = []
    dic = dict()
    
    for n, y in zip(name, yearning):
        dic[n] = y
        
    for p in photo:
        temp = 0
        for person in p:
            if person in dic:
                temp += dic[person]
        
        answer.append(temp)
    
    
    return answer