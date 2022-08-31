# 방법 1: 문자열에서 문자 하나 하나씩
txt = 'hello'

for i in range(len(txt) - 1):
	print(txt[i], txt[i + 1], sep='')

for i in range(len(txt) - 2):
	print(txt[i], txt[i + 1], txt[i + 2], sep='')

# 방법 2-1: 문자열에서 단어 하나 하나씩
txt = 'This is the best skills you have'
words = txt.split()
for i in range(len(words) - 1):
	print(words[i], words[i + 1])

# 방법 2-2: zip함수를 이용함
txt = 'This is the best skills you have'
words = txt.split()
zip_tuples = zip(words, words[1:])
for tup in zip_tuples:
	print(tup[0], tup[1])

# 방법 2-3: zip함수를 이용함
txt = 'hello'
zip_tuples = zip(txt, txt[1:])
for tup in zip_tuples:
	print(tup[0], tup[1], sep='')


# 방법 3: 언패킹을 이용함
txt = 'hello'
for i in range(len(txt) - 2):
	print(txt[i:])

list_txt = [txt[i:] for i in range(len(txt) - 2)]
print(list_txt)
print( list(zip(list_txt)) )
print( list(zip(*list_txt)) )