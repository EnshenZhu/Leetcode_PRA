class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        def findMedian(arr1, arr2, final_index, isEven):
            # m is to track arr1
            # n is to track arr2
            m = 0
            n = 0

            final_sorted_arr = []
            # recall that this final sorted arr does not include all num elements from the arr1 and arr2
            # it only contains num elements from the smallest number to the median number
            # (or the number right after the median number that si existed inside the input arr)

            for i in range(final_index + 1):
                # handle if one of the arrays has reach to the end
                if m >= len(arr1):
                    final_sorted_arr.append(arr2[n])
                    n += 1
                    continue
                elif n >= len(arr2):
                    final_sorted_arr.append(arr1[m])
                    m += 1
                    continue

                # handle the unit comparison when both arrays have not reached to the end
                if arr1[m] <= arr2[n]:
                    final_sorted_arr.append(arr1[m])
                    m += 1
                elif arr1[m] > arr2[n]:
                    final_sorted_arr.append(arr2[n])
                    n += 1

            if isEven:
                return (final_sorted_arr[final_index] + final_sorted_arr[final_index - 1]) / 2
            else:
                return final_sorted_arr[final_index]

        median_index = (len(nums1) + len(nums2)) // 2
        if (len(nums1) + len(nums2)) % 2 == 0:
            return findMedian(nums1, nums2, median_index, isEven=True)
        else:
            return findMedian(nums1, nums2, median_index, isEven=False)


print(Solution.findMedianSortedArrays(Solution, [1, 3], [2]))
print(Solution.findMedianSortedArrays(Solution, nums1=[1, 2], nums2=[3, 4]))
