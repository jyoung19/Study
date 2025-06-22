def solution(quiz):
    answer = []
    
    for q in quiz:
        a, op, b, eq, result = q.split()
        if op == '+':
            if int(a) + int(b) == int(result):
                answer.append("O")
            else:
                answer.append("X")
        if op == '-':
            if int(a) - int(b) == int(result):
                answer.append("O")
            else:
                answer.append("X")
        
    return answer