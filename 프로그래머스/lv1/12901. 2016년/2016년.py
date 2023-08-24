def solution(a, b):
    month_dict = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    day_dict = {0:'FRI', 1:'SAT', 2:'SUN', 3:'MON', 4:'TUE', 5:'WED', 6:'THU'}

    day = b - 1
    for i in range(1, a):
        day += month_dict[i]

    answer = day_dict[day % 7]
    return answer