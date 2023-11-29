def solution(n):
    answer = ''
    
    n = str(n)
    n = sorted(n)
    n.sort(reverse=True)

    for element in n:
        answer += element
    
    return int(answer)