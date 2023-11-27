def solution(myString, pat):
    answer = 0
    temp = []
    
    for i in range(len(myString)-len(pat)+1):
        temp.append(myString[i:i+len(pat)])
    
    print(temp)
    
    for element in temp:
        if element == pat:
            answer += 1
    
    return answer