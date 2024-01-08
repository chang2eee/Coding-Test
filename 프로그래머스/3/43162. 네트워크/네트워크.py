def solution(n, computers):
    answer = 0
    
    graph = dict()
    
    for idx in range(len(computers)):
        graph[str(idx)] = []
        for i in range(len(computers[idx])):
            if idx != i and computers[idx][i] == 1:
                graph[str(idx)].append(str(i))
    
    print(graph)
    
    visited = [False] * len(computers)
    
    for node in graph:
        if not visited[int(node)]:
            dfs(graph, int(node), visited)
            answer += 1
    
    return answer

def dfs(graph, start, visited):
    visited[start] = True
    
    for neighbor in graph[str(start)]:
        if visited[int(neighbor)] == False:
            dfs(graph, int(neighbor), visited)
    
    
    