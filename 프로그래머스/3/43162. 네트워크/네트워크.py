def solution(n, computers):
    answer = 0
    
    network = dict()
    
    # 그래프로 만들기 (딕셔너리 이용)
    for idx, computer in enumerate(computers):
        network[idx] = []
        for i in range(len(computer)):
            if idx != i and computer[i] == 1:
                network[idx].append(i)
    
    visited = [False] * len(computers)
    
    for node in network:
        if visited[node] == False:
            dfs(network, node, visited)
            answer += 1
    
    
    return answer

def dfs(network, start, visited):
    visited[start] = True
    
    for neighbor in network[start]:
        if visited[neighbor] == False:
            dfs(network, neighbor, visited)
