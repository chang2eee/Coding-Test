str = input()

answer = ''

for element in str:
    if element.islower():
        answer += element.upper()
    else:
        answer += element.lower()
    
print(answer)
