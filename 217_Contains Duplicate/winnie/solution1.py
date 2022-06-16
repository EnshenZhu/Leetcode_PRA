class Solution:

    def containsDuplicate(self, nums) -> bool:
        hash_table = {}  # use hashtable
        for value, key in enumerate(nums):
            if key in hash_table:
                return True
            else:
                hash_table[key] = value
        return False


print(Solution.containsDuplicate(Solution, [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
