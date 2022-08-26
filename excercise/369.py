'''
# 10으로 나누면 모든 수의 1의자리에 대해서 확인
# //으로 몫을 찾고 몫이 3, 6, 9인지 확인
for i in range(101):
	if i//10 in (3, 6, 9) or i%10 in (3, 6, 9):
		continue
	print(i, end=' ')
'''
# 문자열로 변환하여 문자 3, 6, 9가 존재하는지 확인
for i in range(101):
	if '3' in str(i) or '6' in str(i) or '9' in str(i):
		continue
	print(i, end=' ')
