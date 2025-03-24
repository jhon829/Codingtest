def solution(a, d, included):
    result = 0
    num = 0
    for i in range(len(included)):
        if i == 0:
            num = a
            if included[i] == True:
                result += num
        else:
            num += d
            if included[i] == True:
                result += num
                
    return result