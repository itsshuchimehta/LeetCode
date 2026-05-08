/**
 * @param {number[]} nums
 * @return {number}
 */
var findClosestNumber = function (nums) {
    let closest = nums[0];
    //Looping through O(N)
    for (let i = 0; i < nums.length; i++) {
        if (Math.abs(nums[i]) < Math.abs(closest)) {
            closest = nums[i];
        }
    }
                        //Looping again O(N)
    if (closest < 0 && nums.includes(Math.abs(closest))) {
        return Math.abs(closest);
    }else {
        return closest;
    }

    // TC: O(2N) -> O(N)
    // SC: O(1)


};