def solution(arr, queries):
    answer = []
    for x, y in queries:
        temp = arr[x]
        arr[x] = arr[y]
        arr[y] = temp 
        
    return arr