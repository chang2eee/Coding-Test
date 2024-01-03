def solution(record):
    answer = []
    
    record_temp = record.copy()
    
    ID_dict = dict()
    
    for element in record_temp:
        elements = element.split()
        status = elements[0]
        user_id = elements[1]
        
        if status == 'Enter' or status == 'Change':
            ID_dict[user_id] = elements[2]

    for element in record:
        elements = element.split()
        status = elements[0] 
        user_id = elements[1]
        
        temp = ''
        
        if status == 'Enter':
            temp += (ID_dict[user_id] + '님이 들어왔습니다.')
        elif status == 'Leave':
            temp += (ID_dict[user_id] + '님이 나갔습니다.')
        else:
            continue
        
        answer.append(temp)
    
    
    return answer