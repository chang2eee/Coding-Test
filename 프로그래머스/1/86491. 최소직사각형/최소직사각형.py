def solution(sizes):
    answer = 0
    width, height = [], []
    
    for size in sizes:
        size.sort()
        
        temp1, temp2 = size
        
        width.append(temp1)
        height.append(temp2)
        
    answer = max(width) * max(height)
    
    return answer