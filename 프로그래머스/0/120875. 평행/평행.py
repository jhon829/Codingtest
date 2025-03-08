def solution(dots):
    answer = 0
    inclination12 = (dots[0][1] - dots[1][1]) / (dots[0][0] - dots[1][0])
    inclination13 = (dots[0][1] - dots[2][1]) / (dots[0][0] - dots[2][0])
    inclination14 = (dots[0][1] - dots[3][1]) / (dots[0][0] - dots[3][0])
    inclination23 = (dots[1][1] - dots[2][1]) / (dots[1][0] - dots[2][0])
    inclination24 = (dots[1][1] - dots[3][1]) / (dots[1][0] - dots[3][0])
    inclination34 = (dots[2][1] - dots[3][1]) / (dots[2][0] - dots[3][0])
    
    if inclination12 == inclination34:
        answer = 1
    elif inclination23 == inclination14:
        answer = 1
    elif inclination13 == inclination24:
        answer = 1
    else:
        answer = 0
        
        
    
    
    return answer