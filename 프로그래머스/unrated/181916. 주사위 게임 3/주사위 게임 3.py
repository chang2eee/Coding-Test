def solution(a, b, c, d):
    answer = 0
    
    if a == b == c == d:
        answer = 1111 * a
        
        
    elif (a == b == c != d):
        p = a
        q = d
        answer = (10 * p + q) ** 2
    elif (b == c == d != a): 
        p = b
        q = a
        answer = (10 * p + q) ** 2
    elif (c == d == a != b): 
        p = c
        q = b
        answer = (10 * p + q) ** 2
    elif (d == a == b != c):
        p = d
        q = c
        answer = (10 * p + q) ** 2
        
        
    elif a == b != c == d:
        p = a
        q = c
        answer = (p + q) * abs(p - q)
    elif b == c != d == a:
        p = b
        q = d
        answer = (p + q) * abs(p - q)
    elif a == c != b == d:
        p = a
        q = b
        answer = (p + q) * abs(p - q)
        
    elif a == b != c != d:
        answer = c * d
    elif a == c != b != d:
        answer = b * d
    elif a == d != b != c:
        answer = b * c
    elif b == c != a != d:
        answer = a * d
    elif b == d != a != c:
        answer = a * c
    elif c == d != a != b:
        answer = a * b
        
    else:
        answer = min(a, b, c, d) 


        
        
    
    return answer