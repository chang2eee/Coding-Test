def solution(intStrs, k, s, l):
    answer = []
    
    for intStr in intStrs:
        temp = int(intStr[s:s+l])
        if temp > k:
            answer.append(temp)
    
    return answer