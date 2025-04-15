def solution(array):
    answer =[]
    t = max(array)
    f = array.index(t)
    answer.append(max(array))
    answer.append(f)
    return answer