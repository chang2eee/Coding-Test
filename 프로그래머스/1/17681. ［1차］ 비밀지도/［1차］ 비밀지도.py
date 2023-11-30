def solution(n, arr1, arr2):
    answer = []
    temp1, temp2 = [], []
    
    for number1, number2 in zip(arr1, arr2):
        temp1.append(bin(number1)[2:].zfill(n))
        temp2.append(bin(number2)[2:].zfill(n))
    
    for number1, number2 in zip(temp1, temp2):
        temp = ''
        for element1, element2 in zip(number1, number2):
            if int(element1) | int(element2):
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)
    return answer