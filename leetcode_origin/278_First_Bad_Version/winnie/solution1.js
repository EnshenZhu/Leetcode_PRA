/**
 * Definition for isBadVersion()
 * 
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */

/**
 * @param {function} isBadVersion()
 * @return {function}
 */
var solution = function (isBadVersion) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
    return function (n) {

        if (n == 1) return n
        var left = 1;
        var right = n;

        while (left <= right) {
            var mid = Math.ceil((left + right) / 2);
            var cursorVersionCheck = isBadVersion(mid);
            var previousVersionCheck = isBadVersion(mid - 1);

            if (cursorVersionCheck === true && previousVersionCheck === false) return mid;
            else if (cursorVersionCheck === true && previousVersionCheck === true) right = mid - 1; // do the left part serach
            else if (cursorVersionCheck === false) left = mid + 1 // do the right part serach
        }
    };
};