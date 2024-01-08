# def solution(n, t, m, p):
#     answer = ''

#     start = 0
#     temp = 0
    
#     num_list = []
    
#     # 2진법
#     if n == 2:
#         while len(num_list) != t * m:
#             temp = bin(start)[2:]
            
#             for i in range(len(temp)):
#                 num_list.append(temp[i])
            
#                 if len(num_list) == t * m:
#                     break
            
#             start += 1
        
#     elif n == 8:
#         while len(num_list) != t * m:
#             temp = oct(start)[2:]
            
#             for i in range(len(temp)):
#                 num_list.append(temp[i])
            
#                 if len(num_list) == t * m:
#                     break
            
#             start += 1
        
#     elif n == 10:
#         while len(num_list) != t * m:
#             temp = str(start)
            
#             for i in range(len(temp)):
#                 num_list.append(temp[i])
            
#                 if len(num_list) == t * m:
#                     break
            
#             start += 1
        
#     elif n == 16:
#         while len(num_list) != t * m:
#             temp = hex(start)[2:]
            
#             for i in range(len(temp)):
#                 num_list.append(temp[i])
            
#                 if len(num_list) == t * m:
#                     break
            
#             start += 1
    
#     else:
#         while len(num_list) != t * m:
#             temp = convert(start, n)
            
#             for i in range(len(temp)):
#                 num_list.append(temp[i])
                
#                 if len(num_list) == t * m:
#                     break
            
#             start += 1
        
#     for i in range(p-1, len(num_list), m):
#         if num_list[i].islower():
#             answer += num_list[i].upper()
#         else:
#             answer += num_list[i]

#     return answer

# def convert(number, base):
#     result = ''
#     temp = ''
    
#     while number != 0:
#         temp += number % base
#         number //= base
    
#     for i in range(len(temp)-1, -1, -1):
#         result += temp[i]

#     return result
    

def convert(number, base):
    temp = '0123456789ABCDEF'
    
    q, r = divmod(number, base)
    
    if q == 0:
        return temp[r]
    else:
        return convert(q, base) + temp[r]

def solution(n, t, m, p):
    answer = ''
    
    num = 0
    
    while True:
        answer += convert(num, n)
        
        if len(answer) >= t * m:
            answer = answer[:t*m]
            
            return answer[p-1:t*m:m]
    
        num += 1
        