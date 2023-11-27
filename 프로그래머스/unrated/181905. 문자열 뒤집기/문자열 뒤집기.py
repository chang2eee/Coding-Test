def solution(my_string, s, e):
    answer = ''
    
    temp1, temp2, temp3 = my_string[:s], my_string[s:e+1], my_string[e+1:]
    
    answer += temp1
    answer += temp2[::-1]
    answer += temp3
    
    return answer