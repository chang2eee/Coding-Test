def solution(spell, dic):
    answer = 2
    for d in dic:
        if not set(spell) - set(d):
            answer = 1
            break
    return answer