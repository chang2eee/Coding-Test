from collections import Counter

def solution(participant, completion):
    participant_counter, completion_counter = Counter(participant), Counter(completion)

    for key in completion_counter:
        participant_counter[key] -= completion_counter[key]

    for key, value in participant_counter.items():
        if value > 0:
            answer = key
            break

    return answer
