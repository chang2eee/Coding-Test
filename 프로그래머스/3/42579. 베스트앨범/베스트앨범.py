def solution(genres, plays):
    answer = []
    
    playtime_dic = dict()
    
    for i in range(len(plays)):
        if genres[i] not in playtime_dic:
            playtime_dic[genres[i]] = [(plays[i], i)]  
        else:
            playtime_dic[genres[i]].append((plays[i], i))
    
    play_dic = dict()
    
    for key, value in playtime_dic.items():
        play_dic[key] = sum(play[0] for play in value)
    
    play_dic = sorted(play_dic.items(), key=lambda x: x[1], reverse=True)
    
    for element in play_dic:
        key = element[0]
        top_two = sorted(playtime_dic[key], key=lambda x: x[0], reverse=True)[:2]
        answer.extend(idx for play, idx in top_two)

    return answer
