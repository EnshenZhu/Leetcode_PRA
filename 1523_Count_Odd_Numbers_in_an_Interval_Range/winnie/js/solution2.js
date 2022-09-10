/**
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var countOdds2 = function (low, high) {
    return high % 2 == 0 && low % 2 == 0 ? parseInt((high - low) / 2) : parseInt((high - low) / 2) + 1
};

export default function countOdds2()

console.log(countOdds2(low = 3, high = 7));
console.log(countOdds2(low = 8, high = 10));
console.log(countOdds2(low = 21, high = 22));