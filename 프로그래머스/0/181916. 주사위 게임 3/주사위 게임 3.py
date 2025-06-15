from collections import Counter

def solution(a, b, c, d):
    counter = Counter([a, b, c, d])
    # [(숫자, 빈도수), (숫자, 빈도수), ...] 형태로 저장
    numbers_count = counter.most_common()  
    
    # case 1 : 네 주사위에서 나온 숫자가 모두 같은 경우
    if (len(counter) == 1):
        return 1111 * a
    
    # case 2 : 세 주사위에서 나온 숫자가 모두 같은 경우
    if (len(counter) == 2) and (numbers_count[0][1] == 3):
        p = numbers_count[0][0]
        q = numbers_count[1][0]
        return (10 * p + q) ** 2
    
    # case 3 : 주사위가 두 개씩 같은 값이 나온 경우
    if (len(counter) == 2) and (numbers_count[0][1] == 2):
        p = numbers_count[0][0]
        q = numbers_count[1][0]
        return ((p + q) * abs(p - q))
    
    # case 4 : 두 주사위에서 나온 숫자가 같고, 나머지 두 주사위에서 나온 숫자가 다른 경우
    if (len(counter) == 3) and (numbers_count[1][1] == 1):
        p = numbers_count[0][0]
        q = numbers_count[1][0]
        r = numbers_count[2][0]
        return q * r
    
    # case 5 : 네 주사위에 적힌 숫자가 모두 다른 경우
    if (len(counter) == 4):
        return min(a, b, c, d)
    