from collections import deque

def bfs(place):
    people = []
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                people.append((i, j))
    
    for person in people:
        queue = deque([person])
        
        visited = [[False] * 5 for _ in range(5)]
        distance = [[0] * 5 for _ in range(5)]
        
        visited[person[0]][person[1]] = True
        
        while queue:
            y, x = queue.popleft()
            
            for i in range(4):
                next_y = y + dy[i]
                next_x = x + dx[i]
                
                if 0 <= next_y < 5 and 0 <= next_x < 5 and not visited[next_y][next_x]:
                    visited[next_y][next_x] = True
                    distance[next_y][next_x] = distance[y][x] + 1
                    
                    if place[next_y][next_x] == 'P' and distance[next_y][next_x] <= 2:
                        return 0
                    elif place[next_y][next_x] == 'O':
                        queue.append((next_y, next_x))
    return 1

def solution(places):
    answer = []
    
    for place in places:
        answer.append(bfs(place))
    
    return answer
