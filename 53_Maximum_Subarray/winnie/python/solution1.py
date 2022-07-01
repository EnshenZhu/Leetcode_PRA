# This script is inspired and refactored from the leetcode practical solution
# The temp_arr and max_arr are added to visualize the target array variation

import copy


class Solution:
    def maxSubArray(self, nums) -> int:
        temp_sum = max_sum = nums[0]
        # we cannot set the temp_sum and  max_sum to be default to 0
        # instead we need to set to nums[0]

        temp_arr = max_arr = [nums[0]]

        for i in nums[1:]:
            temp_arr.append(i)
            temp_sum = sum(temp_arr)
            if sum(temp_arr) < i:
                temp_arr = [i]
                temp_sum = sum(temp_arr)

            if temp_sum > max_sum:
                max_sum = temp_sum
                max_arr = copy.deepcopy(temp_arr)

        return max_sum, max_arr


print(Solution.maxSubArray(Solution, [-2, 1, -3, 4, -1, 2, 1, -5, 4]))
