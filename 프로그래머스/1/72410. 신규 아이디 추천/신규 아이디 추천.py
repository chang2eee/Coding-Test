def solution(new_id):
    answer = ''
    skipper = 'abcdefghijklmnopqrstuvwxyz1234567890-_.'
    skipper = list(skipper)
    
    
    # step 1
    new_id_1 = new_id.lower()
    print('new_id_1: ', new_id_1)

    # step 2
    new_id_2 = ''
    for element in new_id_1:
        if element in skipper:
            new_id_2 += element
        
    print('new_id_2: ', new_id_2)

    # step 3
    new_id_3 = ''
    temp_stack = []
    
    for element in new_id_2:
        if not temp_stack:  # temp_stack : empty
            temp_stack.append(element)
        else:
            if element == '.' and temp_stack[-1] == '.':
                continue
            else:
                temp_stack.append(element)
    
    
    for element in temp_stack:
        new_id_3 += element
        
    print('new_id_3: ', new_id_3)

        
    # step 4
    new_id_4 = ''
    
    if new_id_3 and new_id_3[0] == '.':
        new_id_3 = new_id_3[1:]
    if new_id_3 and new_id_3[-1] == '.':
        new_id_3 = new_id_3[:-1]

    new_id_4 = new_id_3
    
    print('new_id_4: ', new_id_4)


    # step 5
    new_id_5 = ''
    
    if not new_id_4:
        new_id_5 += 'a'
    else:
        new_id_5 = new_id_4
    
    print('new_id_5: ', new_id_5)

    # step 6
    new_id_6 = ''
    
    if len(new_id_5) >= 16:
        for i in range(15):
            new_id_6 += new_id_5[i]
        
        if new_id_6 and new_id_6[-1] == '.':
            new_id_6 = new_id_6[:-1]
    else:
        new_id_6 = new_id_5

    print('new_id_6: ', new_id_6)

    
    # step 7
    new_id_7 = ''
    
    if len(new_id_6) <= 2:
        temp = new_id_6[-1]
        
        while len(new_id_6) != 3:
            new_id_6 += temp
    
    print('new_id_7: ', new_id_7)


    new_id_7 = new_id_6
    answer = new_id_7
        
    return answer