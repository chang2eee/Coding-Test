def solution(wallpaper):
    answer = []
    
    temp_x, temp_y = [], []
    
    for col in range(len(wallpaper)):
        for row in range(len(wallpaper[0])):
            if wallpaper[col][row] == '#':
                temp_x.append(col)
                temp_y.append(row)
                
    answer = [min(temp_x), min(temp_y), max(temp_x)+1, max(temp_y)+1]
    
    
    return answer