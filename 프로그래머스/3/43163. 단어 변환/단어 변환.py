from collections import deque

def solution(begin, target, words):
    answer = 0
    
    visited = [False] * len(words)
    
    queue = deque([(begin, 0)])
    
    while queue:
        current, depth = queue.popleft()
        
        if current == target:
            return depth
        
        for idx, value in enumerate(words):
            if visited[idx] == False and isValid(current, value):
                visited[idx] = True
                queue.append((value, depth+1))
    
    
    return answer

def isValid(start, end):
    result = 0
    
    for s, e in zip(start, end):
        if s != e:
            result +=1
    
    return result == 1