def solution(str_list, ex):
    answer = ''
    
    for element in str_list:
        if ex in element:
            continue
        answer += element
    
    return answer