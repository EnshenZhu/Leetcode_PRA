"""
Build a counting HashMap from string s, then deduct values of each char when iterating string t.
If the value of char is 0 or the char is not in the counting HashMap, return it as the target char.
"""

from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counterS = Counter(s)
        for char in t:
            if char not in counterS or counterS[char] == 0:
                return char
            else:
                counterS[char] -= 1


# Time Complexity --> O(N) --> just iterate string s and t
# Space Complexity --> O(1) --> The counters has maximum 26 buckets for 26 letters

s = "kjhgfdsa"
t = "asdfghjkl"

print(Solution().findTheDifference(s, t))
