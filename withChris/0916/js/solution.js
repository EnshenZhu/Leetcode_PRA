var ArrayChallenge_O_N = (arr) => {

    for (let idx = 2; idx < arr.length; idx++) {
        if ((arr[idx] - arr[idx - 1]) * (arr[idx - 1] - arr[idx - 2]) < 0) {
            return idx - 1;
        }
    }

    return -1;
};

var ArrayChallenge_DC_O_N = (arr) => {
    if (arr.length >= 3) {
        var midIdx = Math.floor(arr.length / 2);
        if ((arr[midIdx + 1] - arr[midIdx]) * (arr[midIdx] - arr[midIdx - 1]) < 0) {
            return midIdx;
        }
        else {
            ArrayChallenge_DC_O_N(arr.slice(0, midIdx));
            ArrayChallenge_DC_O_N(arr.slice(midIdx, arr.length));
        }
    }

    return -1
}

var findPeak = (arr) => {
    let left = 0;
    let right = arr.length - 1;

    while(){
        let mid = math.floor((right - left) / 2)
    }
}

console.log(ArrayChallenge_O_N([-4, -2, 9, 10]))
console.log(ArrayChallenge_O_N([5, 4, 3, 2, 10, 11]))

console.log(ArrayChallenge_DC_O_N([-4, -2, 9, 10]))
console.log(ArrayChallenge_DC_O_N([5, 4, 3, 2, 10, 11]))