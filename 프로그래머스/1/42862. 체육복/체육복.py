def solution(n, lost, reserve):
    real_lost = set(lost) - set(reserve)
    print(real_lost)
    real_reserve = set(reserve) - set(lost)
    print(real_reserve)

    for student in real_reserve:
        if student - 1 in real_lost:
            real_lost.remove(student - 1)
        elif student + 1 in real_lost:
            real_lost.remove(student + 1)

    answer = n - len(real_lost)
    
    return answer