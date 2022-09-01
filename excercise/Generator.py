
def square_numbers(nums):
    for i in nums:
        print('sdfsdf')
        yield i * i
        yield i

my_nums = square_numbers([1, 2, 3, 4, 5])  #1

print(my_nums)

next(my_nums)
next(my_nums)
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
