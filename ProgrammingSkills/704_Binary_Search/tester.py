def firstPositive(arr):
    result = len(arr)
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] > 0:
            right = mid - 1
            result = mid
        else:
            left = mid + 1
    return result


print(firstPositive([-2, -1, -1, 1, 2, 3]))
