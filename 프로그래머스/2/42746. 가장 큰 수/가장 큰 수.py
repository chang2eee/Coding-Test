def solution(numbers):
    def compare(x, y):
        return (int(y + x)) - (int(x + y))

    numbers = list(map(str, numbers))

    numbers.sort(key=lambda x: x*10, reverse=True)

    answer = ''.join(numbers)

    answer = str(int(answer))

    return answer
