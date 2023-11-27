def solution(id_pw, db):
    answer = 'fail'
    
    for info in db:
        if info == id_pw:
            answer = 'login'
        elif info[0] == id_pw[0] and info[1] != id_pw[1]:
            answer = 'wrong pw'
    
    return answer