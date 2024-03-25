def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2])
    print(costs)
    link = set([costs[0][0]])

    while len(link) != n:
        for v in costs:
            if v[0] in link and v[1] in link:
                continue
            if v[0] in link or v[1] in link:
                link.add(v[0])
                link.add(v[1])
                answer += v[2]
                break
                
    return answer