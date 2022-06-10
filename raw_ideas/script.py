# find the not repeated combination of [1,2,3,4]

class Solution:
    def dispNum(self, numlist):
        hashmap = Solution.mapGenerate(numlist)
        return

    def mapGenerate(self, numlist):
        index = 0
        mapping = {}

        for i in numlist:
            mapping[index] = i
            index += 1

        return mapping
