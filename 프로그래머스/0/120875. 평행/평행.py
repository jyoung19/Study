# (x1, y1), (x2, y2)를 잇는 직선1
# (x3, y3), (x4, y4)를 잇는 직선2
# 직선1의 기울기 = (y2 - y1) / (x2 - x1) 와 직선2의 기울기 = (y4 - y3) / (x4 - x3)가 같은지 비교
# 분모를 처리하는 과정에서 부동소수점이 발생할 수 있으니, 곱셈으로 처리
# (y2 - y1) * (x4 - x3) == (y4 - y3) * (x2 - x1)


def solution(dots):
    def is_parallel(a, b, c, d):
        return (b[1] - a[1]) * (d[0] - c[0]) == (d[1] - c[1]) * (b[0] - a[0])

    # 가능한 선분 쌍 조합
    pairs = [
        (0, 1, 2, 3),
        (0, 2, 1, 3),
        (0, 3, 1, 2)
    ]

    for a, b, c, d in pairs:
        if is_parallel(dots[a], dots[b], dots[c], dots[d]):
            return 1
    return 0