def solution(array, height):
    answer = 0
    arraylength = len(array)
    for i in range(arraylength):
        if array[i] > height:
            answer += 1
    return answer