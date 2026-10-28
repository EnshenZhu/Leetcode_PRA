class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        writeIdx = 0  # handle writing for fixing the nums

        # checkIdx-->check on the qualified element for operation
        for checkIdx in range(len(nums)):
            # Step 1: operate on the qualified element
            if (
                    (checkIdx < len(nums) - 1)
                    and (nums[checkIdx] != 0)
                    and (nums[checkIdx] == nums[checkIdx + 1])
            ):
                nums[checkIdx] *= 2
                nums[checkIdx + 1] = 0

            # Step 2: use writeIdx to shift non-zero element to the front
            if nums[checkIdx] != 0:
                if checkIdx != writeIdx:
                    nums[writeIdx], nums[checkIdx] = (
                        nums[checkIdx],
                        nums[writeIdx],
                    )
                writeIdx += 1
        return nums


x = [1, 2, 2, 1, 1, 0]
print(Solution().applyOperations(x))

# It is [1, 4, 2, 0, 0, 0] NOT the original [1, 2, 2, 1, 1, 0]
# Because the applyOperations is an in-place manipulation
print(x)
