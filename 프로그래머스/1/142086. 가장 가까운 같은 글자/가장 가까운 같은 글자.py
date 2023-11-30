def solution(s):
    answer = []
    
    dic = dict()
    
    for idx in range(len(s)):
        if s[idx] not in dic:
            dic[s[idx]] = idx
            answer.append(-1)
        else:
            answer.append(abs(idx - dic[s[idx]]))
            dic[s[idx]] = idx

    
    return answer