from collections import Counter

def solution(participant, completion):
    answer = ''
    
    participant_counter, completion_counter = Counter(participant), Counter(completion)
    
    for key, value in participant_counter.items():
        if key not in completion_counter or value != completion_counter[key]:
            return key
        
    
    return answer