# word = 'level'
word = input('Enter a word: ')
flag = True

## 방법 1
# i = 0
# while i < len(word) // 2:
# 	if word[i] != word[-1 - i]:
# 		print('Not a parlindrome')
# 		flag = False
# 		break
# 	i += 1

## 방법 2
# for i in range(len(word) // 2):
# 	if word[i] != word[-1 - i]:
# 		flag = False
# 		break
# 
# print(f'{word} is a parlindrome?', flag)

# # 방법 3
# print(word == word[::-1])

# 방법 4
print(list(word) == list(reversed(word)))
