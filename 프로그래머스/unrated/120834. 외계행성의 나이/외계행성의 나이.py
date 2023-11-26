def solution(age):
    answer = ''
    age_dic = dict()
    age_dic = {'0': 'a', '1': 'b', '2': 'c', '3': 'd', 
               '4': 'e', '5': 'f', '6': 'g', '7': 'h',
              '8': 'i', '9': 'j'}
    
    for element in str(age):
        answer += age_dic[element]
    
    return answer