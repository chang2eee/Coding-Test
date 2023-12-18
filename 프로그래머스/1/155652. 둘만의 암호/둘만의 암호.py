def solution(s, skip, index):
    answer = ''
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = list(alphabet)
    original_length = len(alphabet)
    
    for word in skip:
        alphabet.remove(word)
    
    modified_length = len(alphabet)
    modified_alphabet = dict()
    
    for idx, alpha in enumerate(alphabet):
        modified_alphabet[alpha] =  alphabet[(idx + index) % modified_length]
    
    for element in s:
        answer += modified_alphabet[element]
    
    
    return answer