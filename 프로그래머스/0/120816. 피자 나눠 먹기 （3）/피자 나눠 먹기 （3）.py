def solution(slice, n):
    answer = 1
    slice2 = slice
    
    if slice >= n:
        answer = 1
    else:
        while slice2 < n:
            slice2 = slice2 + slice
            answer += 1
            
    return answer