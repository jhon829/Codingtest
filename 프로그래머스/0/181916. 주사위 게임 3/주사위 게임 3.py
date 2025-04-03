def solution(a, b, c, d):
    answer = 0
    nums = [a, b, c, d]  # 변수 이름 변경 (list -> nums)
    nums.sort(reverse=True)  # 내림차순 정렬

    if nums[0] == nums[3]:  # 네 숫자가 모두 같은 경우
        answer = nums[0] * 1111
    elif nums[0] == nums[2]:  # 세 숫자가 같은 경우
        answer = (10 * nums[0] + nums[3]) * (10 * nums[0] + nums[3])
    elif nums[1] == nums[3]:
        answer = (10 * nums[1] + nums[0]) * (10 * nums[1] + nums[0])
    elif nums[0] == nums[1] and nums[2] == nums[3]:  # 두 쌍의 숫자가 같은 경우
        answer = (nums[0] + nums[2]) * (nums[0] - nums[2])
    elif nums[0] == nums[1]:  # 첫 번째 쌍만 같은 경우
        answer = nums[2] * nums[3]
    elif nums[1] == nums[2]:  # 두 번째 쌍만 같은 경우
        answer = nums[0] * nums[3]
    elif nums[2] == nums[3]:  # 세 번째 쌍만 같은 경우
        answer = nums[0] * nums[1]
    else:  # 모두 다른 숫자인 경우
        answer = nums[3]

    return answer
