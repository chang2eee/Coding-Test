def solution(arr):    
    length = max(len(arr), len(arr[0]))
    
    for element in arr:
        if len(element) < length:
            for i in range(length - len(element)):
                element.append(0)
        elif len(arr) < length:
            for i in range(length - len(arr)):
                arr.append([0] * length)
                
        
    
    return arr