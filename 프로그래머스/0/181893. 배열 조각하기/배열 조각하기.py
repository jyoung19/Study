def solution(arr, query):
    for i in range(len(query)):
        # 짝수 인덱스
        if i % 2 == 0:
            arr = arr[:query[i] + 1]
        # 홀수 인덱스
        else:
            arr = arr[query[i]:]
    return arr
