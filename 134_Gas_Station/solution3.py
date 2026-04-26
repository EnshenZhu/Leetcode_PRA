# dynamic programming
def canCompleteCircuit(gas, cost):
    start, cur_gas, total_gas = 0, 0, 0
    for i in range(len(gas)):
        cur_gas += gas[i] - cost[i]
        total_gas += gas[i] - cost[i]
        if cur_gas < 0:
            cur_gas = 0
            start = i + 1
    return start if total_gas >= 0 else -1


print(canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
print(canCompleteCircuit([2, 3, 4], [3, 4, 3]))

# Time Complexity: O(n)
# Space Complexity: O(1)
