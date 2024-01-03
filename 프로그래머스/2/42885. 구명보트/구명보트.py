from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()

    people = deque(people)

    while people:
        if len(people) > 1 and people[0] + people[-1] <= limit:
            people.popleft()
            people.pop()
        else:
            people.pop()

        answer += 1

    return answer

print(solution([50, 70, 80, 50], 100))
