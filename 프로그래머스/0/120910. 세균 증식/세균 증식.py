def solution(n, t):
    answer = 1
    for i in range(t):
        answer = answer * 2
    return answer * n