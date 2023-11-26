def solution(arr, k):
    answer = []
    
    for element in arr:
        if k % 2 == 1:
            answer.append(element * k)
        else:
            answer.append(element + k)
    return answer