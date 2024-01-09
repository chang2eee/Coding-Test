from collections import deque

def solution(tickets):
    routes = dict()

    for ticket in tickets:
        departure, arrival = ticket
        if departure not in routes:
            routes[departure] = [arrival]
        else:
            routes[departure].append(arrival)
            routes[departure].sort(reverse=True)

    answer = []

    queue = deque(['ICN'])

    while queue:
        current_airport = queue[-1]

        if current_airport in routes and routes[current_airport]:
            next_airport = routes[current_airport].pop()
            queue.append(next_airport)
        else:
            answer.append(queue.pop())

    answer.reverse()

    return answer



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

#     stack = ['ICN']

#     while stack:
#         current_airport = stack[-1]

#         if current_airport in routes and routes[current_airport]:
#             next_airport = routes[current_airport].pop()
#             stack.append(next_airport)
#         else:
#             answer.append(stack.pop())

#     answer.reverse()

#     return answer



# answer = []

# def solution(tickets):
#     global answer
    
#     start = 'ICN'
    
#     routes = dict()
    
#     for ticket in tickets:
#         departure, arrival = ticket[0], ticket[1]
#         if departure not in routes:
#             routes[departure] = [arrival]
#         else:
#             routes[departure].append(arrival)
#             routes[departure].sort()
            
#     visited = dict()
    
#     for key, value in routes.items():
#         temp = []
        
#         for element in value:
#             if element in routes:
#                 temp.append(element)
        
#         routes[key] = temp
        
#         visited[key] = len(temp)
    
#     print(routes)
#     print(visited)

#     dfs(start, routes, visited, answer)
    
#     return answer

# def dfs(start, routes, visited, answer):
#     if start in visited and visited[start] > 0:
#         visited[start] -= 1
#         answer.append(start)
#         start = routes[start].pop(0)
        
#         dfs(start, routes, visited, answer)
#     else:
#         answer.append(start)
    
#     return 