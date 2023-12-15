from collections import Counter

def solution(X, Y):
    x_counter = Counter(X)
    y_counter = Counter(Y)
    answer = ''

    for i in range(9, -1, -1):
        count = min(x_counter[str(i)], y_counter[str(i)])
        answer += str(i) * count

    if answer == '':
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else:
        return answer