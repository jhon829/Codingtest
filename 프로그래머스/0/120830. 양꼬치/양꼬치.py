def solution(n, k):
    answer = 0
    service = n // 10 
    answer = n * 12000 +  2000 * (k-service)
    return answer