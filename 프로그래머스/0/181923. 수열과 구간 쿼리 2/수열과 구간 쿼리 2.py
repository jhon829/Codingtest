def solution(arr, queries):
    result = []  # 결과를 저장할 리스트
    
    for s, e, k in queries:
        # 범위 [s, e]에 있는 값 중 k보다 큰 값을 필터링
        filtered_values = [arr[i] for i in range(s, e + 1) if arr[i] > k]
        
        # 필터링된 값 중 가장 작은 값을 찾고 결과에 추가
        if filtered_values:
            result.append(min(filtered_values))
        else:
            result.append(-1)  # 조건을 만족하는 값이 없으면 -1 추가
    
    return result

