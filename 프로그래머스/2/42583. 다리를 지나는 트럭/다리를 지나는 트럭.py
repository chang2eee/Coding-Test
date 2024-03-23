from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    
    current =0
    
    while truck_weights:
        answer += 1 # 시간도 어짜피 흐른다
        
        current -= bridge.popleft() # 어짜피 빼야함
        if current + truck_weights[0] <= weight:    # 하나 더
            current += truck_weights[0]
            bridge.append(truck_weights.popleft())
        else:
            bridge.append(0)
    answer += bridge_length # 마지막 트럭이 건너는 시간
            
            
    
    return answer