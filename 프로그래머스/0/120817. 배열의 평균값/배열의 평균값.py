def solution(numbers):
    answer = 0
    result = 0
    for i in range(len(numbers)):
        answer = answer + numbers[i]
    result = float(answer / len(numbers))
    return result