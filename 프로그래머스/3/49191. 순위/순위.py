def solution(n, results):
    answer = 0
    
    win_graph = {(i+1): set() for i in range(n)}
    lose_graph = {(i+1): set() for i in range(n)}
    
    for result in results:
        winner, loser = result
        
        win_graph[loser].add(winner)
        lose_graph[winner].add(loser)
    
    for i in range(1, n+1):
        for winner in win_graph[i]:
            lose_graph[winner].update(lose_graph[i])
        for loser in lose_graph[i]:
            win_graph[loser].update(win_graph[i])
    
    for i in range(1, n+1):
        if len(win_graph[i]) + len(lose_graph[i]) == n-1:
            answer += 1
    
    return answer