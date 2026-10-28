# brute force
def canCompleteCircuit(gas, cost):
    n = len(gas)
    for start in range(n):
        tank = 0
        canComplete = True
        for step in range(n):
            idx = (start + step) % n
            tank += gas[idx] - cost[idx]
            if tank < 0:
                canComplete = False
                break
        if canComplete:
            return start
    return -1


print(canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
print(canCompleteCircuit([2, 3, 4], [3, 4, 3]))

# Time Complexity: O(n^2)
# Space Complexity: O(1)
