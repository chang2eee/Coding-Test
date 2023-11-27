def solution(bin1, bin2):
    a1, a2 = (int(bin1,2), int(bin2,2))
    return format((a1+a2),'b')