N = int(input())

arr = list(map(int, input().split()))

answer = min(arr) * max(arr)

print(answer)