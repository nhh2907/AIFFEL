myarray = arr.array('i', [1, 2, 3])   # 이것은 array입니다. import array를 해야 쓸 수 있습니다.
print(type(myarray))

# 아래 라인의 주석을 풀고 실행하면 에러가 납니다.
#myarray.append('4')    # myarray의 끝에 character '4'를 추가합니다.
print(myarray)

myarray.insert(1, 5)    # myarray의 두번째 자리에 5를 끼워넣습니다.
print(myarray)