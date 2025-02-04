def solution(n):
    answer = 1
    
    for i in range(1, n+1):
        if i * 6 % n == 0:
            return answer
        else:
            answer = answer + 1