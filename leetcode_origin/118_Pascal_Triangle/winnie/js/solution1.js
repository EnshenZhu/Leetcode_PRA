// dynamic programming

/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function (numRows) {
    var result = [[1]];

    for (let i = 1; i < numRows; i++) {
        
        result.push([])

        for (let j = 0; j <= i; j++) {

            if (j == 0 || j == i) {
                result[i].push(1);
            }
            else {
                result[i].push(result[i - 1][j - 1] + result[i - 1][j]);
            }

        }
    }

    return result;

};

console.log(generate(5))