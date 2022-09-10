/**
 * @param {string} s
 * @return {number}
 */

var translate = (roman) => {
    table = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    };
    return table[roman]
}

var romanToInt = function (s) {
    // pre-set the final result to be the translation of the last string element
    result = translate(s[s.length-1]);

    // iterate from the second last string element to the first string elemnet
    for (let idx = s.length - 2; idx >= 0; idx--) {
        if (translate(s[idx]) < translate(s[idx + 1])) result -= translate(s[idx]) // DO subtraction if the forward element has a lower translated value than the latter element
        else result += translate(s[idx]) // DO multiplication if the forward element has a higher translated value than the latter element
    };

    return result
};

console.log(romanToInt("MCMXCIV"))
console.log(romanToInt("LVIII"))
console.log(romanToInt("IVL"))