// find the odd number by iterating from low to high

/**
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var countOdds1 = function (low, high) {
    var count=0;
    for (let num = low; num <= high; num++) {        
        if (num % 2 == 1) {
            count++
        };        
    }
    return count;
};

export default function countOdds1()

// console.log(countOdds1(low = 3, high = 7));
// console.log(countOdds1(low = 8, high = 10));