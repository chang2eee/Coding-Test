def solution(routes):
    answer = 0
    
    routes.sort(key=lambda x:x[1])
    
    key = -30001
    count = 0
    
    for route in routes:
        if route[0] > key:
            count += 1
            key = route[1]
    
    answer = count 
    
    return answer