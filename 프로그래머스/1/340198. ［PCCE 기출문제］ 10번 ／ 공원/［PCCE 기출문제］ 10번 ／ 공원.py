def check(park, size):
    for i in range(0, len(park) - size + 1):
        for j in range(0, len(park[0]) - size + 1):
            # (i, j) 부터 시작해서 size x size 영역이 park 안에 있음
            all_clear = True
            for x in range(size):
                for y in range(size):
                    if park[i + x][j + y] != "-1":
                        all_clear = False
                        break
                if not all_clear:
                    break
            if all_clear:
                return True  # 깔 수 있는 위치 발견!

    
def solution(mats, park):
    for size in sorted(mats, reverse=True):
        if check(park, size):
            return size
    return -1
