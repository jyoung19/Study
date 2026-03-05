import sys

class Deque:
    def __init__(self):
        self.deque = []

    def push_front(self, item):
        # 정수 X를 덱의 앞에 넣는다.
        self.deque.insert(0, item)

    def push_back(self, item):
        # 정수 X를 덱의 뒤에 넣는다.
        self.deque.append(item)

    def pop_front(self):
        # 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다.
        # 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if not self.is_empty():
            print(self.deque.pop(0))
        else:
            print(-1)

    def pop_back(self):
        # 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다.
        # 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if not self.is_empty():
            print(self.deque.pop())
        else:
            print(-1)

    def size(self):
        # 덱에 들어있는 정수의 개수를 출력한다.
        print(len(self.deque))

    def is_empty(self):
        return len(self.deque) == 0

    def empty(self):
        # 덱이 비어있으면 1을, 아니면 0을 출력한다.
        if len(self.deque) == 0:
            print(1)
        else:
            print(0)

    def front(self):
        # 덱의 가장 앞에 있는 정수를 출력한다.
        # 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if not self.is_empty():
            print(self.deque[0])
        else:
            print(-1)

    def back(self):
        # 덱의 가장 뒤에 있는 정수를 출력한다.
        # 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if not self.is_empty():
            print(self.deque[-1])
        else:
            print(-1)

N = int(sys.stdin.readline())
dq = Deque()

for _ in range(N):
    line = sys.stdin.readline().split()
    command = line[0]

    if command == "push_front":
        Deque.push_front(dq, line[1])
    elif command == "push_back":
        Deque.push_back(dq, line[1])
    elif command == "pop_front":
        Deque.pop_front(dq)
    elif command == "pop_back":
        Deque.pop_back(dq)
    elif command == "size":
        Deque.size(dq)
    elif command == "empty":
        Deque.empty(dq)
    elif command == "front":
        Deque.front(dq)
    elif command == "back":
        Deque.back(dq)
