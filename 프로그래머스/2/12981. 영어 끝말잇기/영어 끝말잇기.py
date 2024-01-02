def solution(n, words):
    answer = [0, 0]
    
    player_dict = dict()

    for i in range(n):
        player_dict[i] = []
    
    stack = []

    for idx, word in enumerate(words):
        if word not in stack and (not stack or word[0] == stack[-1][-1]):
            stack.append(word)
            player_dict[idx % n].append(word)
        else:
            answer = [idx % n + 1, len(player_dict[idx % n]) + 1]
            break
    
    return answer