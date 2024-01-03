from math import ceil

def solution(fees, records):
    answer = []
    default_time, default_fee, unit_time, unit_fee = fees
    cars_dict = dict()
    
    for element in records:
        element = element.split(' ')
        time, number, status = element
        
        if number not in cars_dict:
            cars_dict[number] = [[status, time]]
        else:   # number in cars_dict:
            cars_dict[number].append([status, time])
        
    for key, value in cars_dict.items():
        value = sorted(value, key=lambda x:x[1])
    
    print(cars_dict)
    
    usage_dict = dict()
    
    for key, value in cars_dict.items():
        print('value :', value)
        
        if len(value) % 2 == 0: # IN, OUT 다 기록되어 있다
            for i in range(0, len(value), 2):
                temp = value[i:i+2]
                if key not in usage_dict:
                    usage_dict[key] = [getTime(temp[1][1]) - getTime(temp[0][1])]
                else:
                    usage_dict[key].append(getTime(temp[1][1]) - getTime(temp[0][1]))
        
        else: # IN, OUT X
            for i in range(0, len(value), 2):
                temp = value[i:i+2]
                
                if len(temp) == 2:
                    if key not in usage_dict:
                        usage_dict[key] = [getTime(temp[1][1]) - getTime(temp[0][1])]
                    else:
                        usage_dict[key].append(getTime(temp[1][1]) - getTime(temp[0][1]))    
                else:
                    if key not in usage_dict:
                        usage_dict[key] = [getTime('23:59') - getTime(temp[0][1])]
                    else:
                        usage_dict[key].append(getTime('23:59') - getTime(temp[0][1]))  
            
    print(usage_dict)        
    # default_time, default_fee, unit_time, unit_fee = fees            
    
    fees_dict = dict()
    
    for key, value in usage_dict.items():
        if sum(value) > default_time:
            fees_dict[key] = default_fee + ceil((sum(value) - default_time) / unit_time) * unit_fee
        else:
            fees_dict[key] = default_fee
    
    print("fees_dict : ", fees_dict)
    
    fees_dict = sorted(fees_dict.items(), key=lambda x:x[0])
    
    for key, value in fees_dict:
        answer.append(value)
        
    return answer

def getTime(time):
    time = time.split(':')
    
    return int(time[0]) * 60 + int(time[1])