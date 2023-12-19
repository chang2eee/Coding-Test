def solution(s):
    answer = []
    
    cnt = 0
    zero_count = 0

    while s != '1':
        cnt += 1
        
        ones_count = s.count('1')
        
        zero_count += len(s) - ones_count
        
        s = bin(ones_count)[2:]

    answer = [cnt, zero_count]
    
    return answer
