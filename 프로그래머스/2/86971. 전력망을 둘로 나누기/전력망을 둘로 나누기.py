def dfs(node, parent, graph, n, min_diff):
    count = 1
    for neighbor in graph[node]:
        if neighbor != parent:
            count += dfs(neighbor, node, graph, n, min_diff)
    diff = abs(n - 2*count)
    
    min_diff[0] = min(min_diff[0], diff)
    return count

def solution(n, wires):
    answer = 0
    graph = dict()
    
    for start, end in wires:
        if start not in graph:
            graph[start] = [end]
        else:
            graph[start].append(end)
        if end not in graph:
            graph[end] = [start]
        else:
            graph[end].append(start)
            
    min_diff = [float('inf')]
    for v1, v2 in wires:
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        dfs(v1, v2, graph, n, min_diff)
        dfs(v2, v1, graph, n, min_diff)
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    answer = min_diff[0]
    return answer