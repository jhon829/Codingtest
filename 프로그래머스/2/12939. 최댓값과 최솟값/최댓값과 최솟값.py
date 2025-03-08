def solution(s):
    answer = ''
    list1 = [int(i) for i in s.split()]
    max1 = max(list1)
    min1 = min(list1)
    answer = str(min1) + ' ' + str(max1)
    return answer