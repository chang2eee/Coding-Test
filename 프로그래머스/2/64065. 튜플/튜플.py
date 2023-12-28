def solution(s):
    answer = []
    temp = ''
    dic = dict()

    s = s[1:-1].split('},')
    
    for subset in s:
        subset = subset.replace('{', '').replace('}', '')
        elements = subset.split(',')
        
        for element in elements:
            if element in dic:
                dic[element] += 1
            else:
                dic[element] = 1
    
    answer = [int(key) for key, value in sorted(dic.items(), key=lambda x: x[1], reverse=True)]
    
    return answer