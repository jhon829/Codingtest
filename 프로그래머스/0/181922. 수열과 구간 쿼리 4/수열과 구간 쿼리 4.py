def solution(arr, queries):
    answer = []
    for t in queries:
        for i in range(t[0],t[1]+1):
            if i%t[2]==0:
                arr[i] += 1
    return arr
