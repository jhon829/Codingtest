def solution(want, number, discount):
    answer = 0
    buy = []
    for i in range(len(want)):
        for j in range(number[i]):
            buy.append(want[i])
            
    for k in range(len(discount)):
        if sorted(discount[k:k+10]) == sorted(buy):
            answer += 1
    return answer