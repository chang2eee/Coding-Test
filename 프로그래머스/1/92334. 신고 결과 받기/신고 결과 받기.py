from collections import Counter

def solution(id_list, report, k):
    answer = []
    
    user = dict()
    check = dict()
    count_reports = Counter()
    
    # Dictionary로 만들기
    for element in id_list:
        user[element] = []
        check[element] = False
    
    # 신고자 : 신고당한 사람
    for rep in set(report):
        rep = rep.split(' ')
        user[rep[0]].append(rep[1])
        count_reports[rep[1]] += 1
    
    # 정지된 유저 확인
    suspended_users = set()
    for reported_user, count in count_reports.items():
        if count >= k:
            suspended_users.add(reported_user)
    
    # 정지된 유저에 대한 메일 발송 및 결과 저장
    for reporter, reported_users in user.items():
        suspended_count = sum(1 for u in reported_users if u in suspended_users)
        answer.append(suspended_count)
    
    return answer