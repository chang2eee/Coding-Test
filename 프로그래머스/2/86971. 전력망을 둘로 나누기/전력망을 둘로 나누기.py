def solution(n, wires):
    # 그래프 생성
    graph = [[] for _ in range(n + 1)]
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    min_diff = float('inf')

    # DFS 함수 정의
    def dfs(node, parent):
        nonlocal min_diff
        count = 1
        for neighbor in graph[node]:
            if neighbor != parent:
                count += dfs(neighbor, node)
        diff = abs(n - 2 * count)
        min_diff = min(min_diff, diff)
        return count

    # 각 전선을 끊어가며 송전탑 개수 차이 계산
    for v1, v2 in wires:
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        dfs(v1, v2)
        dfs(v2, v1)
        graph[v1].append(v2)
        graph[v2].append(v1)

    return min_diff