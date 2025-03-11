def solution(A, B):
    answer = 0
    count = 0
    
    if A == B:
        return 0
    else:
        List_A = list(A)
        List_B = list(B)
        for i in List_A:
            List_A = List_A[-1:] + List_A[:-1]
            count = count + 1
            if List_A == List_B:
                answer = count
                return count
    return -1