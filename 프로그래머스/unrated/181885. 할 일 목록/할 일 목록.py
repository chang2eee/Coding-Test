def solution(todo_list, finished):
    answer = []
    temp_dic = dict()

    for todo, status in zip(todo_list, finished):
        temp_dic[todo] = status

    for key, value in temp_dic.items():
        if not value:
            answer.append(key)

    return answer
