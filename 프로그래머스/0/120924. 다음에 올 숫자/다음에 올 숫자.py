def solution(common):
    n = len(common) + 1
    
    # 등차수열
    if (common[1] - common[0]) == (common[2] - common[1]):
        d = common[1] - common[0]
        return common[0] + (n-1) * d
    
    # 등비수열
    if (common[1] / common[0]) == (common[2] / common[1]):
        r = common[1] / common[0]
        return common[0] * r ** (n-1)
