from collections import deque

def solution(begin, target, words):
    queue = deque([(begin, 0)]) 
    visited = set() 
    
    while queue:
        current, depth = queue.popleft()
        if current == target:
            return depth

        for word in words:
            if word not in visited and can_convert(current, word):
                visited.add(word)
                queue.append((word, depth + 1))

    return 0  

def can_convert(word1, word2):
    return sum(1 for a, b in zip(word1, word2) if a != b) == 1
