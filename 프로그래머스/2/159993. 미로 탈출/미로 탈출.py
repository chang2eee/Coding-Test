from collections import deque

def bfs(maps, start, end):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 시작점
    start_y, start_x = 0, 0
    
    # 탈출지점 / 레버위치
    end_y, end_x = 0, 0
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == start:
                start_y, start_x = i, j
            if maps[i][j] == end:
                end_y, end_x = i, j
                
    # 방문여부 확인 
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    
    # 이동거리
    distance = 0
    
    queue = deque([(start_y, start_x, distance)])
    
    # 방문할 곳 남아있을 시
    while queue:
        y, x, distance = queue.popleft()
        
        # 탈출조건
        if y == end_y and x == end_x:
            return distance
        
        # 탈출 불가
        for i in range(4):
            # 추가방문
            next_y = y + dy[i]
            next_x = x + dx[i]
            
            # 다음 방문할 장소가 maps 내부에 위치하는지 확인 and 막혀있는 길이 아닌지 확인
            if 0 <= next_y <= len(maps)-1 and 0 <= next_x <= len(maps[0])-1 and maps[next_y][next_x] != 'X':
                # 방문한 기록 없음
                if visited[next_y][next_x] == False:
                    queue.append((next_y, next_x, distance+1))
                    visited[next_y][next_x] = True
    
    
    return -1

def solution(maps):
    # 레버 먼저 건드리기
    path1 = bfs(maps, 'S', 'L')
    
    # 레버 건드린 후 탈출시도
    path2 = bfs(maps, 'L', 'E')

    
    # 둘 다 길이 존재
    if path1 != -1 and path2 != -1:
        return path1 + path2
    
    return -1