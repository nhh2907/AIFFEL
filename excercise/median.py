def median(nums):
    nums.sort()
    size = len(nums)
    index = size // 2
    if size % 2 == 0:
        i_even_upper = index  # 4번째 값
        i_even_lower = index - 1  # 3번째 값
        mid = (nums[i_even_lower] + nums[i_even_upper])/ 2
    else:
        mid = nums[index]
    return mid


li = [1, 2, 3, 4, 5, 6]

print(median(li))
