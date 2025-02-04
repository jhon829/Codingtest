def solution(n):
    answer = 0
    
    for i in range(n+1):
        if 7 * i / n < 1:
            answer = answer + 1
        else:
            return answer
