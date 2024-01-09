def solution(operations):
    answer = []
    
    temp_list = []
    
    for op in operations:
        if op == 'D 1':
            temp_list = temp_list[:-1]
        elif op == 'D -1':
            temp_list = temp_list[1:]
        else:
            op = op.split()
            
            temp_list.append(int(op[1]))
            temp_list.sort()
        
    if not temp_list:
        return [0, 0]
    else:
        answer = [temp_list[-1], temp_list[0]]
    
    
    return answer