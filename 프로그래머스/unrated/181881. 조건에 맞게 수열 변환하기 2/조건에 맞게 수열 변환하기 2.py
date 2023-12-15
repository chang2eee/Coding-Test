def solution(arr):
    answer = 0
    temp = set()

    while True:
        container = []

        for element in arr:
            if element >= 50 and element % 2 == 0:
                container.append(element / 2)
            elif element < 50 and element % 2 == 1:
                container.append(element * 2 + 1)

        container.sort()
        arr = container  # Update arr with the new container

        if tuple(arr) in temp:
            break

        temp.add(tuple(arr))
        answer += 1

    return answer - 1
