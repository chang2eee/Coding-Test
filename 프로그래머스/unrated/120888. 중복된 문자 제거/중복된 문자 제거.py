def solution(my_string):
    temp_set = set()
    answer = ''

    for char in my_string:
        if char not in temp_set:
            temp_set.add(char)
            answer += char

    return answer