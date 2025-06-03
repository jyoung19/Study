def time_to_sec(t):
    m, s = map(int, t.split(":"))
    return m * 60 + s


def sec_to_time(s):
    return f"{s // 60:02d}:{s % 60:02d}"


def skip_op(pos, op_start, op_end):
    if op_start <= pos <= op_end:
        return op_end
    else:
        return pos

    
def solution(video_len, pos, op_start, op_end, commands):
    video_length = time_to_sec(video_len)
    pos = time_to_sec(pos)
    op_start = time_to_sec(op_start)
    op_end = time_to_sec(op_end)
    
    pos = skip_op(pos, op_start, op_end)
    
    for command in commands:
        # 10초 후로 이동
        if command == "next":
            pos = min(video_length, pos + 10)
        elif command == "prev":
            pos = max(0, pos - 10)
        pos = skip_op(pos, op_start, op_end)
    
    return sec_to_time(pos)