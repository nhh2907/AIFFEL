# 숫 입력받고 리스트에 넣기
def numbers():
    X = []
    inp = input('Enter a number: <Enter key> to quit ')
    while inp != "":
        try:
            number = float(inp)
            X.append(number)
        except ValueError:
            print('>>> Not a number! Ignored..')
        inp = input('Enter a number: <Enter key> to quit ')
    if len(X) > 1:
        return X


# 평균
def means(X):
    total = 0
    n = len(X)
    for i in range(n):
        total = total + X[i]
    return total/n


# 표준편차
def std_dev(X, means):
    variance = 0  # variance 의미: 분산(편차의 제곱의 합)
    n = len(X)
    for i in range(n):
        variance = variance + (X[i] - means)**2
    return (variance/n) ** 0.5

def main():
    X = numbers()
    if X is None:
        return
    avg = means(X)
    std = std_dev(X, avg)
    # print(__dict__)
    print(f'표준편차 {std}, 평균 {avg}, 리스트 {X}')


if __name__ == '__main__':
    main()
