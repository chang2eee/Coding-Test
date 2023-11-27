def solution(arr, k):
    result = []
    seen_numbers = set()

    for num in arr:
        if num not in seen_numbers:
            result.append(num)
            seen_numbers.add(num)

    while len(result) < k:
        result.append(-1)

    return result[:k]
