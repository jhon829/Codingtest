def solution(n):
    answer = 0
    for i in range(n):
        if i*i == n:
            return 1
    return 2