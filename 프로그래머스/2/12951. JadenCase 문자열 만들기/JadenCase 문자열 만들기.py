def solution(s):
    s_list = s.split(" ")
    jaden_case_list = [word.capitalize() for word in s_list]
    return " ".join(jaden_case_list)
