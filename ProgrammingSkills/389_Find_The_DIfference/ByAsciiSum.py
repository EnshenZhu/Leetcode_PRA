class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum_s = sum(ord(char) for char in s)
        sum_t = sum(ord(char) for char in t)
        return chr(sum_t - sum_s)


# Time Complexity --> O(N)
# Space Complexity --> O(1)

s = "kjhgfdsa"
t = "asdfghjkl"

print(Solution().findTheDifference(s, t))
