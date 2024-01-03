from collections import deque

def solution(begin, target, words):
    n = len(words)
    visited = [False] * n
    
    queue = deque([(begin, 0)]) 
    
    while queue:
        current, depth = queue.popleft()
        if current == target:
            return depth

        for i, word in enumerate(words):
            if not visited[i] and can_convert(current, word):
                visited[i] = True
                queue.append((word, depth + 1))

    return 0  

def can_convert(word1, word2):
    count = 0
    
    for a, b in zip(word1, word2):
        if a != b:
            count += 1
    
    return count == 1
 
