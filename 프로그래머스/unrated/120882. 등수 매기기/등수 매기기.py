def solution(score):
    answer = []
    
    score_avg = []
    
    for numbers in score:
        score_avg.append(sum(numbers) / len(numbers))
    
    sorted_avg = sorted(score_avg, reverse=True)
    
    for avg in score_avg:
        answer.append(sorted_avg.index(avg) + 1)
    
    return answer