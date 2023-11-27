def solution(myString, pat):
    result = ""
    last_index = myString.rfind(pat)  

    if last_index != -1:  
        result = myString[:last_index + len(pat)] 
    
    return result