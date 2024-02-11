from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    queue1, queue2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    
    max_count = len(queue1) * 3
    
    if sum1 == sum2:
        return 0
    elif (sum1 + sum2) % 2 == 1:
        return -1
    
    while True:
        if sum1 > sum2:
            temp = queue1.popleft()
            queue2.append(temp)
            sum1 -= temp
            sum2 += temp
            answer += 1
        elif sum1 < sum2:
            temp = queue2.popleft()
            queue1.append(temp)
            sum1 += temp
            sum2 -= temp
            answer += 1
        else:
            break
        
        if answer == max_count:
            return -1
    return answer