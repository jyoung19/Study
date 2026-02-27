import sys

T = sys.stdin.readline()
lines = [sys.stdin.readline().strip() for _ in range(1, int(T)+1)]

for line in lines:
    words = line.split()
    for word in words:
        result = "".join(word[::-1])
        print(result, end=" ")
    print()