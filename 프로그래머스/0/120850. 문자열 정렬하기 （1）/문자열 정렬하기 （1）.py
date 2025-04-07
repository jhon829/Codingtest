def solution(my_string):
    answer = list(my_string)
    result =[]
    for i in answer:
        if i.isdigit():
            result.append(int(i))
    result.sort()
    return result