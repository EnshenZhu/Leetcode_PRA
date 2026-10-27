1. If the total amount of gas is less than the total cost, return -1.
2. If the total amount of gas is greater than or equal to the total cost, then even if gas runs out midway, starting from a different location will allow a full circuit.
3. We can use a greedy approach.
4. Suppose we start from the first gas station, we can accumulate the capital gain/loss on each station. The station with the most accumulated capital lost is the hardest time to pass through. Therefore, the solution is the station that right after the "hardest time" station.