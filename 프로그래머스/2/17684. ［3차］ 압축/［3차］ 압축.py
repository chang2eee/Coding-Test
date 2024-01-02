def solution(msg):
    answer = []
    
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    alphabet_dict = dict()
    
    for idx, alpha in enumerate(alphabet):
        alphabet_dict[alpha] = idx + 1
    
    idx = 27
    start, end = 0, 1
    
    while end <= len(msg):
        s = msg[start:end]
        
        if s in alphabet_dict:
            end += 1
        else:
            answer.append(alphabet_dict[s[:-1]])
            alphabet_dict[s] = idx
            idx += 1
            start = end - 1
    
    answer.append(alphabet_dict[s])
    
    return answer
