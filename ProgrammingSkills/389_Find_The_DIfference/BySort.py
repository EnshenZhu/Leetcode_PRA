"""
Sort s and t string first to get sorted_s and sorted_t.
Then iterate sorted_s to compare each char to find the diff.
If there are no diff, then sorted_t[-1] is the target char.
"""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        for i in range(len(sorted_s)):
            if sorted_s[i] != sorted_t[i]:
                return sorted_t[i]

        return sorted_t[-1]

# Time Complexity --> O(NlogN) --> The sorting
# Space Complexity --> O(N) --> To store sorted_s and sorted_t

s = "kjhgfdsa"
t = "asdfghjkl"

print(Solution().findTheDifference(s, t))
