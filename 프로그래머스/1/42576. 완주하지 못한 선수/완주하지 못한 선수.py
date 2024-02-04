from collections import Counter

def solution(participant, completion):
    answer = ''
    
    participant_counter = Counter(participant)
    completion_counter = Counter(completion)
    
    for key in completion_counter.keys():
        participant_counter[key] -= completion_counter[key]
        
    for key, value in participant_counter.items():
        if value > 0:
            answer = key
            return answer