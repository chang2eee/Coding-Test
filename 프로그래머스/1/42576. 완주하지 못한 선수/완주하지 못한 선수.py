from collections import Counter

def solution(participant, completion):
    answer = ''
    
    participant_counter, completion_counter = Counter(participant), Counter(completion)
    
    for key, value in participant_counter.items():
        if value != completion_counter[key]:
            answer = key
            break
        
        if key not in completion_counter:
            answer = key
            break
    
    return answer