def solution(n):
    answer = 0
    n1 = 0
    n2 = 1
    sum = 0
    n3 = 0
    if n == 2:
        answer = sum % 1234567
    for i in range(n-1):
        sum = n1 + n2
        temp = n2
        n2 = n1 + n2
        n1 = temp
    return sum % 1234567