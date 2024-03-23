answer = 0

def dfs(k, dungeons, visited, count):
    global answer
    answer = max(answer, count)
    
    for i in range(len(dungeons)):
        if visited[i] == False and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k-dungeons[i][1], dungeons, visited, count+1)
            visited[i] = False


def solution(k, dungeons):
    global answer
    
    visited = [False] * len(dungeons)
    dfs(k, dungeons, visited, 0)
    
    return answer