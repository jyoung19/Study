def solution(bandage, health, attacks):
    current = health  # 현재 체력
    attack_dict = {time: dmg for time, dmg in attacks}
    last_attack = attacks[-1][0]  # 마지막 공격 시간
    cnt = 0  # 연속 성공 시간
    
    # 마지막 공격까지 반복
    for sec in range(1, last_attack+1): 
        # 공격이 있을 경우
        if sec in attack_dict:
            current -= attack_dict[sec]
            if current <= 0:
                return -1
            cnt = 0   
            
        # 공격이 없을 경우
        else:
            current += bandage[1]
            cnt += 1
            # 연속 성공할 경우
            if cnt == bandage[0]:
                current += bandage[2]
                cnt = 0
            # 현재 체력이 최대 체력보다 큰 경우
            if current > health:
                current = health
                        
    return current
