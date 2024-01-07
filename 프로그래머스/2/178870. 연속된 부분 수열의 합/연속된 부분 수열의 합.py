def solution(sequence, k):
    answer = []
    
    temp = []
    current_sum = 0
    start = 0

    for end in range(len(sequence)):
        current_sum += sequence[end]
        
        while current_sum > k:
            current_sum -= sequence[start]
            start += 1
        
        if current_sum == k:
            temp.append([start, end])

    if temp:
        answer = min(temp, key=lambda x: x[1] - x[0])

    return answer
