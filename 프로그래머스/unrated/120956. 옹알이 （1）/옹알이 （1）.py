def solution(babbling):
    answer = 0
    
    baby = ['aya', 'ye', 'woo', 'ma']
    
    for element in babbling:
        count = 0
        word = ''
        
        for i in element:
            word += i
            if word in baby:
                word = ''
                count += 1
        
        if len(word) == 0 and count > 0:
            answer += 1
    
    return answer