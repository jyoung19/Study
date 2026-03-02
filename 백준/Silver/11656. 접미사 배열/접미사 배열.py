word = input()
word_list = []

while(len(word) != 0):
    word_list.append(word)
    word = word[1:]

print(*sorted(word_list), sep="\n")

'''

# 1. 
# print("\n".join(sorted(word_list)))

# 2. 
# for word in sorted(word_list):
#     print(word)

# 3. 
# print(*sorted(word_list), sep="\n")

'''