# Solution

## Approach 1: Optimized Brute Force

### Intuition

This algorithm doesn't reliably run under the time limit here on LeetCode. We'll still look briefly at it though, as in an interview scenario it would be a great start if you're struggling to come up with a better approach.

Calculate the sum of all subarrays, and keep track of the best one. To actually generate all subarrays would take O(N<sup>3</sup>) time, but with a little optimization, we can achieve brute force in O(N<sup>2</sup>) time. The trick is to recognize that all of the subarrays starting at a particular value will share a common prefix.

### Algorithm

1. Initialize a variable maxSubarray = -infinity to keep track of the best subarray. We need to use negative infinity, not 0, because it is possible that there are only negative numbers in the array.
2. Use a for loop that considers each index of the array as a starting point.
3. For each starting point, create a variable currentSubarray = 0. Then, loop through the array from the starting index, adding each element to currentSubarray. Every time we add an element it represents a possible subarray - so continuously update maxSubarray to contain the maximum out of the currentSubarray and itself.
4. Return maxSubarray.

### Python Solution:

    class Solution:
        def maxSubArray(self, nums: List[int]) -> int:
            max_subarray = -math.inf
            for i in range(len(nums)):
                current_subarray = 0
                for j in range(i, len(nums)):
                    current_subarray += nums[j]
                    max_subarray = max(max_subarray, current_subarray)
        
        return max_subarray

## Approach 2: Dynamic Programming, Kadane's Algorithm

## Approach 3: Divide and Conquer (Advanced)