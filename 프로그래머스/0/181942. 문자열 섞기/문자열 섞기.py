def solution(str1, str2):
    answer = ''
    L1 = list(str1)
    L2 = list(str2)
    
    for i in range(len(L1)):
        answer += L1[i] + L2[i]
    
    
    return str(answer)