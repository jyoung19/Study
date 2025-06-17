def solution(numbers):
    
    n1 = max(numbers)
    numbers.pop(numbers.index(n1))
    
    n2 = max(numbers)
    numbers.pop(numbers.index(n2))

    return n1 * n2