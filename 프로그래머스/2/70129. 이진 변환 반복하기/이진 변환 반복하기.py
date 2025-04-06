def solution(s):
    answer = []
    count1 = 0
    count2 = 0
    while s != '1':
        for i in s:
            if i == '0':
                count1 += 1
        s = s.replace("0","")
        s = bin(len(s))[2:]

        count2 += 1
        
    return [count2, count1]