def solution(numbers):
    answer = []
    number1 = numbers.copy()
    number2 = numbers.copy()
    first = max(number1)
    number1.remove(first)
    second = max(number1)
    
    minus_first = min(number2)
    number2.remove(minus_first)
    minus_second = min(number2)
    
    if first*second >= minus_first*minus_second:
        return first*second
    else:
        return minus_first*minus_second