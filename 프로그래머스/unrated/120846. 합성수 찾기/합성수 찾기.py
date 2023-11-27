def solution(n):
    def count_divisors(num):
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        return count

    composite_count = 0

    for i in range(4, n + 1):
        if count_divisors(i) >= 3:
            composite_count += 1

    return composite_count