def solution(emergency):
    answer = []
    answer2 = []
    
    answer2 = sorted(emergency)
    answer2.reverse()
    
    for i in emergency:
        answer.append(answer2.index(i)+1)
    return answer