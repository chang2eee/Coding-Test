def solution(lottos, win_nums):
    answer = []
    
    dic = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    correct = 0
    
    possiblity = lottos.count(0)
    
    for lotto in lottos:
        if lotto in win_nums:
            correct += 1
    
    answer = [dic[correct+possiblity], dic[correct]]
    
    return answer