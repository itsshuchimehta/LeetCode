/**
 * @param {number[]} nums
 * @return {number}
 */
var findClosestNumber = function(nums) {
    let closest = nums[0];
    

    for (let i = 0; i < nums.length; i++){
        // Condition 1: Is it strictly closer to zero?
        if(Math.abs(nums[i]) < Math.abs(closest)){
            closest = nums[i];
        }
        // Condition 2: Is it the SAME distance, but a larger number?
        else if(Math.abs(nums[i]) === Math.abs(closest) && nums[i] > closest){
            closest = nums[i];
        }
   
    }

    return closest;

};