def solution(box, n):
    answer = 0
    
    floor = (box[0] // n) * (box[1] // n)
    height = box[2] // n
    
    answer = floor * height
    
    return answer