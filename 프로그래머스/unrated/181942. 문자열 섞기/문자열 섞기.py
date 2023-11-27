def solution(str1, str2):
    answer = ''
    
    for element1, element2 in zip(str1, str2):
        answer += element1
        answer += element2
    
    return answer