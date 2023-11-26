def solution(n_str):
    answer = ''
    index = 0
    
    for string in n_str:
        if string == '0':
            index += 1
            continue
        else:
            answer = n_str[index:]
            break
    
    return answer