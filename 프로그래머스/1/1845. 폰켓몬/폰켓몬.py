def solution(nums):
    count = 0
    size_count = {}
    for size in nums:
        if size in size_count:
            size_count[size] += 1
        else:
            size_count[size] = 1
    sorted_counts = sorted(size_count.values(), reverse=True)
    you_take = int(sum(sorted_counts)/2)
    answer = min(you_take,len(sorted_counts))
    return answer