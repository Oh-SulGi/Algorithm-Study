def solution(myStr):
    answer = []
    for i in myStr.split('a'):
        for j in i.split('b'):
            for k in j.split('c'):
                if k != '':
                    answer.append(k)
    if len(answer) > 0:
        return answer
    else:
        return ['EMPTY']