import sys

while True:
    line = sys.stdin.readline().rstrip('\n')
    if line == ".":
        break

    stack = []
    flag = True

    for char in line:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] !='(':
                flag = False
                break
            stack.pop()
        elif char == ']':
            if not stack or stack[-1] !='[':
                flag = False
                break
            stack.pop()

    if flag and not stack:
        print("yes")
    else:
        print("no")