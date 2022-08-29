import itertools

# Cartesian Product
for element in itertools.product([1, 2, 3], ['a', 'b'], [4, 5]):
    print(element)

# https://stackoverflow.com/questions/533905/get-the-cartesian-product-of-a-series-of-lists

# print(tuple(itertools.product(['파이썬', 'AI'], ['Noh', 'Kim', 'Lee'])))
# for i, j in itertools.product(['파이썬', 'AI'], ['Noh', 'Kim', 'Lee']):
# 	print(f"{i}는 {j}입니다")