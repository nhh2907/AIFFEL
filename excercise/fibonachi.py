memory = {1:1, 2:1}

# 재귀함수를 부를 때마다 이미 계산한 피보나치 수는 딕셔너리에 저장하고, 딕셔너리에 있는 경우 바로 반환함
def fibonachi(n):
    if n in memory:
        number = memory[n]
    else:
        number = fibonachi(n-2) + fibonachi(n-1)
        memory[n] = number
    return number

for i in range(1, 10):
    answer = fibonachi(i)
    print(answer)

# print(fibonachi(10))
