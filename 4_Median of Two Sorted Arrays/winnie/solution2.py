class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        result = nums1 + nums2
        result.sort()

        if len(result) % 2 == 0:
            mid = len(result) // 2
            return (result[mid] + result[mid - 1]) / 2
        else:
            mid = len(result) // 2
            return result[mid]


print(Solution.findMedianSortedArrays(Solution, [1, 3], [2]))
print(Solution.findMedianSortedArrays(Solution, nums1=[1, 2], nums2=[3, 4]))
