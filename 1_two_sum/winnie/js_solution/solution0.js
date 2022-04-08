/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var twoSum = function(nums, target) {
    var map=new Map
    
    for (var i=0;i<nums.length;i++){
        var counter=target-nums[i]
        
        if (map.has(counter)){
            return [map.get(counter),i]
        } 
        
        map.set(nums[i],i)
    }
};

console.log(twoSum([1,2,3],3))