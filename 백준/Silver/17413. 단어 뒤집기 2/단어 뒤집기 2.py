S = input()
answer = []
tmp = []
in_tag = False

for char in S:
    if char == '<':
        while tmp:
            answer.append(tmp.pop())
        in_tag = True
        answer.append(char)
    elif char == '>':
        in_tag = False
        answer.append(char)
    elif in_tag == True:
        answer.append(char)
    elif char == ' ':
        while tmp:
            answer.append(tmp.pop())
        answer.append(char)
    else:
       tmp.append(char)

while tmp:
    answer.append(tmp.pop())

print("".join(answer))