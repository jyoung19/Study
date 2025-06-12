str = input()
new_str = ""

for i in range(len(str)):
    # 소문자 -> 대문자
    if 96 < ord(str[i]) < 123 :
        new_str += chr(ord(str[i]) - 32)
    # 대문자 -> 소문자
    else:
        new_str += chr(ord(str[i]) + 32)
    
print(new_str)
