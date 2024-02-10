from collections import Counter

def solution(phone_book):
    answer = True
    
    phone_book.sort(key=lambda x:len(x))
    
    phone_book_counter = Counter(phone_book)    
    
    for phone_number in phone_book:
        temp = ''
        for number in phone_number:
            temp += number
            
            if temp in phone_book_counter and temp != phone_number:
                answer = False
                return answer
    
    return answer