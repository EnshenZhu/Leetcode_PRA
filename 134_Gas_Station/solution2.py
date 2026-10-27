# dynamic programming
def canCompleteCircuit(gas, cost):
    tank, min_gas, ans = 0, 0, 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if min_gas > tank:
            min_gas = tank
            ans = i + 1
    return ans if tank >= 0 else -1


print(canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
print(canCompleteCircuit([2, 3, 4], [3, 4, 3]))

# Time Complexity: O(n)
# Space Complexity: O(1)
