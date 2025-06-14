def solution(numer1, denom1, numer2, denom2):
    
    # 분수의 덧셈
    denom3 = denom1 * denom2
    numer3 = numer1 * denom2 + numer2 * denom1  
    
    # 기약분수로 나타내기
    for i in range(min(numer3, denom3), 1, -1):
        if (numer3 % i == 0) and (denom3 % i == 0):
            numer3 //= i
            denom3 //= i
            break
        
    return (numer3, denom3)