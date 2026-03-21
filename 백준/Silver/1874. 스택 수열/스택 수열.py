import sys
# 1. 표준 입력보다 빠른 sys.stdin.readline을 쓰기 위해 불러옵니다.
n = int(sys.stdin.readline())

# 2. 데이터를 담을 바구니들을 준비합니다.
stack = []  # 숫자를 쌓아둘 스택
ans = []    # '+', '-' 기호를 순서대로 저장할 리스트
count = 1   # 스택에 넣을 '다음 숫자' (1부터 시작해서 n까지 올라감)
find = True # 수열을 만들 수 있는지 없는지 판단하는 '깃발(Flag)'

# 3. n번 반복하며 수열의 숫자(target)를 하나씩 확인합니다.
for _ in range(n):
    target = int(sys.stdin.readline())

    # [PUSH 과정] 
    # 내가 지금 뽑아야 할 숫자(target)가 아직 스택에 안 들어왔다면?
    # 들어올 때까지 count를 1씩 늘리며 스택에 계속 넣습니다.
    while count <= target:
        stack.append(count) # 스택에 숫자 넣기
        ans.append("+")     # push 했으니까 '+' 기록
        count += 1          # 다음에 넣을 숫자는 1 증가

    # [POP 과정]
    # 이제 스택의 맨 위(stack[-1])를 확인합니다.
    if stack[-1] == target:
        # 만약 맨 위 숫자가 내가 찾던 target과 같다면?
        stack.pop()         # 스택에서 꺼내기
        ans.append("-")     # pop 했으니까 '-' 기록
    else:
        # 만약 맨 위 숫자가 target이 아니라면? (더 큰 숫자가 위에 쌓여있다면)
        # 스택은 나중에 넣은 게 먼저 나와야 하므로(LIFO), 이 순서는 절대 불가능!
        find = False        # "안 된다"고 깃발 표시
        break               # 더 볼 것도 없으니 반복문 탈출

# 4. 최종 결과 출력
if not find:
    # 깃발이 False라면 "불가능" 출력
    print("NO")
else:
    # 깃발이 True라면 저장해둔 '+', '-'를 한 줄씩 출력
    # (for문 대신 '\n'.join(ans)를 쓰면 더 빨라요!)
    for i in ans:
        print(i)