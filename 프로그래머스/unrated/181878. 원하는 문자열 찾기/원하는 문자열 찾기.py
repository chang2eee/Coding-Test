def solution(myString, pat):
    answer = 0
    
    myString, pat = myString.lower(), pat.lower()
    
    if pat in myString:
        answer = 1
    
    return answer