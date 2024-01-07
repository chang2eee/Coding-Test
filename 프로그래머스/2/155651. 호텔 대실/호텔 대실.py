def solution(book_time):
    answer = 0
    
    book_time = sorted(book_time, key=lambda x: x[0])
    
    idx = 0
    room = dict()
    
    for i in range(len(book_time)):
        room[i] = []
        
    for start, end in book_time:
        allocated = False
        for key, value in room.items():
            if not value or getTime(start) >= value[-1] + 10:
                room[key].append(getTime(end))
                allocated = True
                break 
        
        if not allocated:
            room[idx].append(getTime(end))
            idx += 1
    
    for key, value in list(room.items()):
        if not value:
            del room[key]
    
    answer = len(room)
    
    return answer

def getTime(time):
    time = time.split(':')
    return int(time[0]) * 60 + int(time[1])