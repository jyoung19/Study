def solution(sides):
    sides.sort()
    a, b, c = sides
    
    if c < a + b:
        return 1
    else:
        return 2