"""
Use XOR to find the difference between two strings.
Recall:
    0 ^ 0 = 0
    0 ^ 1 = 1
    1 ^ 0 = 1
    1 ^ 1 = 0
"""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result=0
        for char in s+t:
            result ^= ord(char)
        return chr(result)

# Time Complexity --> O(N)
# Space Complexity --> O(1)

s = "kjhgfdsa"
t = "asdfghjkl"

print(Solution().findTheDifference(s, t))
