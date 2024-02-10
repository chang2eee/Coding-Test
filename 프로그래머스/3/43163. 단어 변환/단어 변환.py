from collections import deque

def solution(begin, target, words):
    answer = 0
    
    n = len(words)
    
    visited = [False] * n
    
    queue = deque([(begin, 0)])
    
    while queue:
        current, depth = queue.popleft()
        
        if current == target:
            return depth
        
        for idx, word in enumerate(words):
            if visited[idx] == False and can_convert(current, word):
                visited[idx] = True
                queue.append((word, depth+1))
    
    
    return answer

def can_convert(word1, word2):
    count = 0
    
    for a, b in zip(word1, word2):
        if a != b:
            count += 1
    
    return count == 1