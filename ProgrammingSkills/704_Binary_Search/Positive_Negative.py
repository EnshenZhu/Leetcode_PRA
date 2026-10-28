class Solution:
    def FirstPositive(self, nums: list) -> int:
        result = len(nums)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= 0:
                left = mid + 1
            else:
                right = mid - 1
                result = mid
        return result

    def FirstNoneNegative(self, nums: list) -> int:
        result = len(nums)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < 0:
                left = mid + 1
            else:
                right = mid - 1
                result = mid
        return result


print(Solution().FirstPositive([-2, -1, -1, 1, 2, 3]))
print(Solution().FirstNoneNegative([-2, -1, -1, 1, 2, 3]))
print(Solution().FirstPositive([-3, -1, 0, 0, 1, 3, 5, 7, 9]))
print(Solution().FirstNoneNegative([-3, -1, 0, 0, 1, 3, 5, 7, 9]))

print(Solution().FirstNoneNegative([0, 0]))
print(Solution().FirstNoneNegative([-1]))
