def solution(my_string, letter):
    answer = []
    for string in my_string:
        if string == letter:
            pass
        else:
            answer.append(string)
    return (''.join(answer))