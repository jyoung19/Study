from collections import deque

N, K = map(int, input().split())
d = deque()
answer = []

# d = deque(range(1, N+1))
for _ in range(1, N+1):
    d.append(_)

# while d:
#    d.rotate(-(K-1))
#    answer.append(d.popleft())

while(len(d) != 0):
    for _ in range(K-1):
        d.append(d[0])
        d.popleft()
    answer.append(d[0])
    d.popleft()

result = ", ".join(map(str, answer))
print(f"<{result}>")

'''

N=7, K=3

[ 1, 2, 3, 4, 5, 6, 7 ]
3
[ 4, 5, 6, 7, 1, 2 ]
6
[ 7, 1, 2, 4, 5 ]
2
[ 4, 5, 7, 1 ]
7
[ 1, 4, 5 ]
5
[ 1, 4 ]
1
[ 4 ]
4

'''