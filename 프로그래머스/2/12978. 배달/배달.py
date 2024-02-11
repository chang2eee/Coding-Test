def make_graph(N, roads):
    graph = {i: [] for i in range(1, N + 1)}  # 그래프 초기화

    # 양방향으로 간선 추가
    for road in roads:
        a, b, c = road
        graph[a].append((b, c))
        graph[b].append((a, c))

    return graph

import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

def solution(N, road, K):
    graph = make_graph(N, road)
    distances = dijkstra(graph, 1)
    count = 0

    for distance in distances.values():
        if distance <= K:
            count += 1

    return count