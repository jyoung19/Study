def solution(my_string):
    answer = []
    for string in my_string:
        answer.insert(0, string)
    return (''.join(answer))