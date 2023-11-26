def solution(rsp):
    answer = ''
    dic = dict()
    
    dic = {'2': '0', '0': '5', '5': '2'}
    
    for element in rsp:
        answer += dic[element]
    
    return answer
