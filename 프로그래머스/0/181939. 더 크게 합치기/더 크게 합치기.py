def solution(a, b):
    answer = 0
    str1 = str(a) + str(b)
    str2 = str(b) + str(a)
    int1 = int(str1)
    int2 = int(str2)
    
    if int1 > int2:
        answer = int1
    else:
        answer = int2
    
    return answer