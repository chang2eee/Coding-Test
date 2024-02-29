def solution(dirs):
    answer = 0
    
    directions = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    start_x, start_y = 0, 0
    
    visited = set()
    
    for element in dirs:
        next_x = start_x + directions[element][0]
        next_y = start_y + directions[element][1]
        
        route = ((start_x, start_y, next_x, next_y))
        route_reverse = ((next_x, next_y, start_x, start_y))
        
        if -5 <= next_x <= 5 and -5 <= next_y <= 5:
            visited.add(route)
            visited.add(route_reverse)
            
            start_x, start_y = next_x, next_y
    
    answer = len(visited) // 2
    
    return answer