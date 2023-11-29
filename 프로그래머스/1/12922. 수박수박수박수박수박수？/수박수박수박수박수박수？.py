def solution(n):
    answer = ''
    
    soo, bak = '수', '박'
    
    for i in range(n):
        if i % 2 == 0:
            answer += soo
        else:
            answer += bak
    
    return answer