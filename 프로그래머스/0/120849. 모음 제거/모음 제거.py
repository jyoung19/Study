def solution(my_string):
    vowel = ['a', 'e', 'i', 'o', 'u']
    answer = []
    
    for string in my_string:
        if string in vowel:
            pass
        else:
            answer.append(string)
            
    return (''.join(answer))