import math

def solution(numer1, denom1, numer2, denom2):
    
    # 분수의 덧셈
    denom3 = denom1 * denom2
    numer3 = numer1 * denom2 + numer2 * denom1  
    
    # 기약분수로 나타내기 (최대공약수로 나누기)
    gcd = math.gcd(numer3, denom3)
    numer3 //= gcd
    denom3 //= gcd
        
    return (numer3, denom3)