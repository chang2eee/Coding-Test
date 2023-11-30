def solution(arr):
    answer = []
    
    for number in arr:
        if not answer:
            answer.append(number)
            
        else:
            if answer[-1] == number:
                continue
            else:
                answer.append(number)
    
    
    
    return answer