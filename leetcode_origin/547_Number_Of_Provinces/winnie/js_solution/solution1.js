// This solution encounter a Time Limit Exceeded

/**
 * @param {number[][]} isConnected
 * @return {number}
 */
var findCircleNum = function (isConnected) {
    // const graphMap={};
    const visted = new Set();

    var count = 0;

    const bfs = (src) => {
        const queue = [src]

        while (queue.length > 0) {
            const current = queue.shift();
            visted.add(current);

            for (let j = 0; j < isConnected[current].length; j++) {
                const neighbor = isConnected[current][j]
                if (!(visted.has(neighbor)) && neighbor == 1) queue.push(j)
            }
        }

        count += 1
    }

    for (let i = 0; i < isConnected.length; i++) {
        if (!(visted.has(i))) {
            visted.add(i);
            // const currentCity=[];
            // currentCity.push(i);
            bfs(i);
        }
    }

    return count

};

console.log(findCircleNum(isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
// console.log(findCircleNum(isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]))