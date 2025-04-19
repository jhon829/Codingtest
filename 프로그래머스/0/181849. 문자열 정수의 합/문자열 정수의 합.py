def solution(num_str):
    answer = 0
    num = int(num_str)
    while(num > 0):
        answer += num % 10
        num = num // 10
    return answer