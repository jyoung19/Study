from collections import Counter

def solution(array):
    # [[3,3],[1,1],[2,1],[4,1]] 처럼 [[값, 빈도수]] 형태로 저장
    counter = Counter(array).most_common()
    
    # 최빈값이 여러 개인 경우
    if (len(counter) > 1) and (counter[0][1] == counter[1][1]): 
        return -1
    
    # 최빈값이 1개인 경우
    else:
        return counter[0][0]