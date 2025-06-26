def solution(my_string, overwrite_string, s):
    l1 = len(my_string)
    l2 = len(overwrite_string)
    
    if l1 - l2 == s:
        answer = my_string[:s] + overwrite_string
    else:
        answer = my_string[:s] + overwrite_string + my_string[s+l2:]
    return answer