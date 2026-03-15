address = input()

if '::' in address:
    parts = address.split('::')
    left = [g for g in parts[0].split(':') if g]
    right = [g for g in parts[1].split(':') if g]
    res = left + ['0']*(8 - len(left) - len(right)) + right
else:
    res = address.split(':')

for i in range(len(res)):
    res[i] = res[i].zfill(4)

print(":".join(res))