def solution(numbers, hand):
    answer = ''
    
    keypad = {1: [0, 0], 2: [0, 1], 3: [0, 2], 
              4: [1, 0], 5: [1, 1], 6: [1, 2],
              7: [2, 0], 8: [2, 1], 9: [2, 2],
              '*': [3, 0], 0: [3, 1], '#': [3, 2]
             }
    
    right_start, left_start = keypad['#'], keypad['*']
    
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left_start = keypad[number]
        elif number in [3, 6, 9]:
            answer += 'R'
            right_start = keypad[number]
        else:
            right_distance = abs(keypad[number][0] - right_start[0]) + abs(keypad[number][1] - right_start[1])
            left_distance = abs(keypad[number][0] - left_start[0]) + abs(keypad[number][1] - left_start[1])
            
            if right_distance < left_distance:
                answer += 'R'
                right_start = keypad[number]
            elif right_distance > left_distance:
                answer += 'L'
                left_start = keypad[number]
            else:
                if hand == 'right':
                    answer += 'R'
                    right_start = keypad[number]
                elif hand == 'left':
                    left_start = keypad[number]
                    answer += 'L'
                else:
                    continue
    
    return answer
