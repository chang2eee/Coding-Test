def solution(q, r, code):
    answer = ''
    dic = dict()
    
    for i in range(q):
        dic[i] = []
        
    for i in range(len(code)):
        dic[i%q].append(code[i])
    
    for element in dic[r]:
        answer += element
    
    return answer