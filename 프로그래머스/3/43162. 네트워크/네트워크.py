def solution(n, computers):
    answer = 0
    
    network = dict()
    for idx, computer in enumerate(computers):
        network[idx] = []
        for i in range(len(computer)):
            if idx != i and computer[i] == 1:
                network[idx].append(i)

    visited =[False] * n
    
    for node in network:
        if visited[node] == False:
            dfs(network, node, visited)
            answer +=1
    return answer

def dfs(network, node, visited):
    visited[node] = True
    
    for neighbor in network[node]:
        if visited[neighbor] == False:
            dfs(network, neighbor, visited)