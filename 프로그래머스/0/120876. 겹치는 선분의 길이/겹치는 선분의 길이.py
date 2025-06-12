def solution(lines):
    answer = 0

    # 수직선 201개 표시 1차원 배열
    line_arr = [0] * 201

    # lines 순회
    for s, e in lines:

        # 음수를 없애기 위한 100씩 추가
        s = s + 100
        e = e + 100

        # 배열의 표식을 위한 s ~ e - 1 범위까지 순회
        # 마지막을 포함하지 않는 이유는 경계선에 대한 중복 체킹을 방지하기 위함
        for i in range(s, e):

            # 이미 한 번은 확인 되었으면, 정답 추가
            # 삼 중 이상 중첩을 막기 위해 조건문을 1로 제한
            if line_arr[i] == 1:
                answer += 1

            # 선분 체킹
            line_arr[i] += 1

    return answer