def solution(my_string, alp):
    answer = [my_string[i].upper() if my_string[i] == alp else my_string[i] for i in range(len(my_string))]
    return ''.join(answer)