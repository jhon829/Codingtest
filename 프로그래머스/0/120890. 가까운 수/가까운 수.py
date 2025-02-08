def solution(array, n):
    array.sort()
    min_diff = float('inf')
    answer = None
    
    for i in array:
        curr_diff = abs(i - n)
        if curr_diff < min_diff or (curr_diff == min_diff and i < answer):
            min_diff = curr_diff
            answer = i
            
    return answer
