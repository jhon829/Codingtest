def solution(numLog):
    answer = ''
    num = 0
    for i in range(1, len(numLog)):
        num = numLog[i] - numLog[i-1]
        if num == 1:
            answer += 'w'
        elif num == -1:
            answer +='s'
        elif num == 10:
            answer +='d'
        else:
            answer +='a'
        
    return answer