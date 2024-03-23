from collections import Counter

def solution(genres, plays):
    answer = []
    
    temp_dic = dict()
    for g, p in zip(genres, plays):
        if g not in temp_dic:
            temp_dic[g] = p
        else:
            temp_dic[g] += p
    
    temp_dic = sorted(temp_dic.items(), key=lambda x:x[1], reverse=True)
    
    genres_plays_dic = dict()   # 장르, 노래 재생횟수
    for i in range(len(genres)):
        if genres[i] not in genres_plays_dic:
            genres_plays_dic[genres[i]] = [(i, plays[i])]
        else:
            genres_plays_dic[genres[i]].append((i, plays[i]))
            genres_plays_dic[genres[i]] = sorted(genres_plays_dic[genres[i]], key=lambda x:x[1], reverse=True)
    
    for element in temp_dic:
        if len(genres_plays_dic[element[0]]) < 2:
            answer.append(genres_plays_dic[element[0]][0][0])
        else:
            for i in range(2):
                answer.append(genres_plays_dic[element[0]][i][0])
    
    return answer