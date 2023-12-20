def solution(n, words):
    answer = [0, 0]
    used_words = set()  
    stack = []  
    
    for idx, word in enumerate(words):
        if idx > 0 and (words[idx - 1][-1] != word[0] or word in used_words):
            # 이전 단어의 끝말과 맞지 않거나 이미 사용한 단어인 경우
            answer = [(idx % n) + 1, (idx // n) + 1]
            return answer
        
        stack.append(word)  
        used_words.add(word)  
    
    return answer