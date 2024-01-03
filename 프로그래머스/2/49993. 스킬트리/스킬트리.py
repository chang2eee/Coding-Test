def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        temp = ''
        
        for element in skill_tree:
            if element in skill:
                temp += element
            
        if skill[:len(temp)] == temp:
            answer += 1
        
    return answer