def solution(video_len, pos, op_start, op_end, commands):
    
    video_len_minute = int(video_len.split(':')[0])
    video_len_second = int(video_len.split(':')[1])
    video_length = video_len_minute * 60 + video_len_second
    pos_minute = int(pos.split(':')[0])
    pos_second = int(pos.split(':')[1])
    pos_length = pos_minute * 60 + pos_second   
    
    
    # 오프닝 건너뛰기
    def op(op_start, op_end, pos_length):
        op_start_minute = int(op_start.split(':')[0])
        op_start_second = int(op_start.split(':')[1])
        op_start_length = op_start_minute * 60 + op_start_second

        op_end_minute = int(op_end.split(':')[0])
        op_end_second = int(op_end.split(':')[1])
        op_end_length = op_end_minute * 60 + op_end_second   

        if (op_start_length <= pos_length) and (pos_length <= op_end_length):
            pos_length = op_end_length
        
        return pos_length
    
    
    pos_length = op(op_start, op_end, pos_length)
    
    for command in commands:
        pos_length = op(op_start, op_end, pos_length)
            
        # 10초 후로 이동
        if command == "next":
            if video_length - pos_length < 10:
                pos_length = video_length
            else: 
                pos_length += 10
        
            
        # 10초 전으로 이동
        if command == "prev":
            if pos_length < 10:
                pos_length = 0
            else: 
                pos_length -= 10
    
    
    pos_length = op(op_start, op_end, pos_length)
    
    ans_minute = pos_length // 60
    ans_second = pos_length % 60
    
    answer = f"{ans_minute:02d}:{ans_second:02d}"
    
    return answer