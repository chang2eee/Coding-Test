def solution(arr, delete_list):
    answer = []
    
    for element in delete_list:
        if element in arr:
            arr.remove(element)
        
    
    return arr