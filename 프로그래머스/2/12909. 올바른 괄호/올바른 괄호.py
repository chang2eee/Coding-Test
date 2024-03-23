def solution(s):
    if s[0] == ')':
        return False

    temp = []
    for element in s:
        if len(temp) == 0:
            temp.append(element)
        else:
            if temp[-1] == '(' and element == ')':
                temp.pop()
            else:
                temp.append(element)
    
    if len(temp) != 0:
        return False


    return True