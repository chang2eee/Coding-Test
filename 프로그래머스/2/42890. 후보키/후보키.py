from itertools import combinations

def solution(relation):
    col = len(relation)
    row = len(relation[0])

    #가능한 속성의 모든 인덱스 조합 
    combi = []
    for i in range(1, row+1):
        combi.extend(combinations(range(row), i))
        
    #유일성
    unique = []
    for i in combi:
        tmp = [tuple([item[key] for key in i]) for item in relation]

        if len(set(tmp)) == col:    # 유일성
            put = True
            
            for x in unique:
                if set(x).issubset(set(i)):  # 최소성
                    put = False
                    break
                    
            if put: unique.append(i)
    return len(unique)