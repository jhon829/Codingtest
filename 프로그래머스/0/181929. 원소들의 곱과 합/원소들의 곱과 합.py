def solution(num_list):
    num_powsum = 0
    num_mulx = 1
    for i in range(len(num_list)):
        num_mulx *= num_list[i]
        num_powsum += num_list[i]
    num_powsum = num_powsum ** 2
    if num_mulx < num_powsum:
        return 1
    else:
        return 0