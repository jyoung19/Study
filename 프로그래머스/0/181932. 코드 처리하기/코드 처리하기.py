def solution(code):
    mode = 0
    ret = []

    for i in range(len(code)):
        # 문자가 "1"이면 mode를 바꿈
        if code[i] == '1':
            mode = 1 - mode
            continue

        if mode == 0 and i % 2 == 0:
            ret.append(code[i])
        elif mode == 1 and i % 2 == 1:
            ret.append(code[i])

    return ''.join(ret) if ret else "EMPTY"