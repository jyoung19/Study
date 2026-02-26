import sys
from itertools import combinations

data = []

for line in sys.stdin:
    if line.strip() == '0':
        break
    data.append(line.strip())

    lst = list(map(int, line.split()))
    k = lst[0]
    lst = lst[1:]

    result = sorted(combinations(lst, 6))
    for com in result:
        for num in com:
            print(num, end=' ')
        print()

    print()