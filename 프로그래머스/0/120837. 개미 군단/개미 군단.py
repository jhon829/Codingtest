def solution(hp):
    answer1 = 0
    answer2 = 0
    answer3 = 0
    
    
    answer1 = hp // 5
    answer2 = (hp - 5 * answer1) // 3
    answer3 = (hp - 5 * answer1) % 3
    power = answer1 + answer2 + answer3
    return power