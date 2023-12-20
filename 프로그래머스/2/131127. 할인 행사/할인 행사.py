from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    want_dic = dict(zip(want, number))
    
    for i in range(len(discount)-9):
        temp = discount[i:i+10]
        
        temp_counter = Counter(temp)
        
        check = True
        
        for key, value in want_dic.items():
            if temp_counter.get(key, 0) < value:
                check = False
                break
        
        if check:
            answer += 1
    
    return answer
