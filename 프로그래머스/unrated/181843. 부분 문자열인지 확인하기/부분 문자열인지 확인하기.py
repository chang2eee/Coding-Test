def solution(my_string, target):
    answer = 0
    
    len_my_string = len(my_string)
    len_target = len(target)

    for i in range(len_my_string - len_target + 1):
        substring = my_string[i:i + len_target]
        if substring == target:
            answer = 1
            return answer

    return answer
