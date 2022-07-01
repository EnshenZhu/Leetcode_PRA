def maxSubArray(nums):
    if len(nums) == 1:
        return nums[0]

    sum = nums[0]

    for num in nums[1:]:
        sum += num

        # if num is greater than current sum, start sum over
        if num > sum:
            sum = num

    return sum


print(maxSubArray([-2, 1, -3]))
