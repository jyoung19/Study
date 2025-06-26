def solution(picture, k):
    answer = []
    
    for row in picture:
        stretched_row = ''.join(char * k for char in row)
        for _ in range(k):
            answer.append(stretched_row)
            
    return answer