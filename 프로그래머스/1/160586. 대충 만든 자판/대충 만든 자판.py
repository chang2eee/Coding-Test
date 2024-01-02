def solution(keymap, targets):
    answer = []
    keymap_dict = dict()
    
    for keys in keymap:
        for idx, value in enumerate(keys):
            if value not in keymap_dict:
                keymap_dict[value] = idx + 1
            else:   # if value in keymap_dict:
                keymap_dict[value] = min(idx + 1, keymap_dict[value])
            
    for target in targets:
        count = 0
        for element in target:
            if element in keymap_dict:
                count += keymap_dict[element]
            else:
                count = -1
                break
        answer.append(count)
    
    return answer