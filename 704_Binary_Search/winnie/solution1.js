/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
    var left = 0;
    var right = nums.length - 1;

    while (left <= right) {
        var mid = Math.floor((right + left) / 2);
        if (nums[mid] == target) return mid;
        else if (nums[mid] < target) {
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
    }

    return -1;
};

console.log(search(nums = [-1, 0, 3, 5, 9, 12], target = 9));
console.log(search(nums = [-1, 0, 3, 5, 9, 12], target = 2));
console.log(search(nums = [5], target = 5));