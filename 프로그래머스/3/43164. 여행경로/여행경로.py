def solution(tickets):
    answer = []
    
    visited = [False]*len(tickets)
    
    def dfs(airport, path):
        if len(path) == len(tickets)+1:
            answer.append(path)
            return
        
        for idx, ticket in enumerate(tickets):
            if airport == ticket[0] and visited[idx] == False:
                visited[idx] = True
                dfs(ticket[1], path+[ticket[1]])
                visited[idx] = False
        
        
    dfs("ICN", ["ICN"])
    
    answer.sort()

    return answer[0]


# from collections import deque

# def solution(tickets):
#     routes = dict()

#     for ticket in tickets:
#         departure, arrival = ticket
#         if departure not in routes:
#             routes[departure] = [arrival]
#         else:
#             routes[departure].append(arrival)
#             routes[departure].sort(reverse=True)  

#     answer = []

#     queue = deque(['ICN'])

#     while queue:
#         current_airport = queue[0]

#         if current_airport in routes and routes[current_airport]:
#             next_airport = routes[current_airport].pop()
#             queue.append(next_airport)
        
#         answer.append(queue.popleft())


#     return answer