from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    cache = deque()
    
    # 대문자 -> 소문자
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
    
    if cacheSize == 0:
        answer = 5 * len(cities)
        return answer
    
    for city in cities:
        if city not in cache: # 없다
            answer += 5
            if len(cache) >= cacheSize:
                cache.popleft()
                cache.append(city)
            else:
                cache.append(city)
        else:   #city in cache
            answer += 1
            if len(cache) >= cacheSize:
                cache.remove(city)
                cache.append(city)
            else:
                cache.remove(city)
                cache.append(city)
                
                    
    
    
    return answer