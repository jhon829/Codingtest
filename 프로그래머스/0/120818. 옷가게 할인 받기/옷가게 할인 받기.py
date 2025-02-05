def solution(price):
    answer = 0
    
    if price >= 500000:
        answer = int(price * 0.80)
    elif price >= 300000:
        answer = int(price * 0.90)
    elif price >= 100000:
        answer = int(price * 0.95)
    else:
        answer = price
    return answer