# 这题要反复看

# Dynamic Programming

# This script is inspired and refactored from the leetcode practical solution
# This version is to submit to the leetcode

class Solution:
    def maxSubArray(self, nums) -> int:
        temp_sum = max_sum = nums[0]

        for element in nums[1:]:
            temp_sum += element
            if temp_sum < element:
                temp_sum = element
            max_sum = max(max_sum, temp_sum)

        return max_sum


print(Solution.maxSubArray(Solution, [-2, 1, -3, 4, -1, 2, 1, -5, 4]))
