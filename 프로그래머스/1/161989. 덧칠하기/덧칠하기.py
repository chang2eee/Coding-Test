def solution(n, m, section):
    answer = 0
    section = [s-1 for s in section]
    section.sort()
    
    visited = [False] * n
    
    for sec in section:
        if visited[sec] == False:
            end_idx = min(sec+m, n)
            
            for i in range(sec, end_idx):
                visited[i] = True
            answer += 1
    
    return answer