def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)
    
    list_length = len(A)
    for i in range(list_length):
        answer += A[i] * B[i]

    return answer