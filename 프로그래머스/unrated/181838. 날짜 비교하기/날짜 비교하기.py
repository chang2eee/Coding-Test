def solution(date1, date2):
    answer = 0
    year1, month1, day1 = date1
    year2, month2, day2 = date2

    if year1 < year2 or (year1 == year2 and month1 < month2) or (year1 == year2 and month1 == month2 and day1 < day2):
        answer = 1
    else:
        answer = 0

    return answer