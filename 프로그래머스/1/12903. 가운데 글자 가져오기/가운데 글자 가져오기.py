def solution(s):
    answer = ''
    length = len(s)
    medium = length // 2
    
    if length % 2 == 0:
        answer = s[medium-1: medium+1]
    else:
        answer = s[medium]
    return answer