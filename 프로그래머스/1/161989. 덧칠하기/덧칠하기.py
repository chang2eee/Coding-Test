def solution(n, m, section):
    answer = 0
    
    checked = [False] * n
    section = [sec - 1 for sec in section]
    
    section.sort()
    
    for sec in section:
        if not checked[sec]:
            end_idx = min(sec + m, n)
            
            for idx in range(sec, end_idx):
                checked[idx] = True
            answer += 1
    
    return answer
