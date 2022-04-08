def maxSubArray(nums):
    if len(nums) == 1:
        return nums[0]

    sum = max_sum = nums[0]

    for num in nums[1:]:
        sum += num

        # if num is greater than current sum, start sum over
        if num > sum:
            sum = num

        max_sum = max(max_sum, sum)

    return max_sum


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
