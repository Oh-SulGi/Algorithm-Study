def solution(a, b):
    answer1 = int(''.join([str(a), str(b)]))
    answer2 = 2 * a * b
    return max(answer1, answer2)