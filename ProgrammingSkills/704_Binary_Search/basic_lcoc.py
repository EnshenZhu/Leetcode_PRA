class Solution:
    def BinarySearch(self, nums: list, target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid


print(Solution().BinarySearch([1, 3, 5, 7, 9], 3))
print(Solution().BinarySearch([1, 3, 5, 7, 9], 4))
