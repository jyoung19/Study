def solution(array, height):
    array.append(height)  # 머쓱이의 키를 배열에 추가 
    cnt = 0
    
    for i in range(len(array)):
        if array[i] > height:
            cnt += 1
            
    return cnt