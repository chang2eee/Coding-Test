def solution(names):
    answer = []
    
    for index in range(0, len(names), 5):
        answer.append(names[index])
    
    return answer