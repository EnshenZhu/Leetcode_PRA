# apply with the hashmap

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # create a hashmap
        hashmap = {}

        for i in range(len(nums)):
            counter = target - nums[i]
            if counter in hashmap:
                return [hashmap[counter], i]
            hashmap[nums[i]] = i


target_ls = Solution.twoSum(Solution, [2, 5, 3, 1, 6, 5], target=8)
print(target_ls)
