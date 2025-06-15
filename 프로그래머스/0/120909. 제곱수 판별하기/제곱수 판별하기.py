import math

def solution(n):
    # 제곱근이 정수인지 확인
    if math.sqrt(n) % 1 == 0:
        return 1
    else:
        return 2