def solution(array, n):
    array.sort()
    answer = 0
    com = n+100
    for i in array:
        if abs(i-n) < com:
            com = abs(i-n)
            answer = i
    return answer