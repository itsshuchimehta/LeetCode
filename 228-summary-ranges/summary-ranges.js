/**
 * @param {number[]} nums
 * @return {string[]}
 */
var summaryRanges = function(nums) {
    const result = [];
  let i = 0;

  // Scan each range starting point once
  while (i < nums.length) {
    const start = nums[i];

    // Extend while numbers stay consecutive
    while (i + 1 < nums.length && nums[i + 1] === nums[i] + 1) {
      i++;
    }

    const end = nums[i];

    // Add single value or full range based on boundaries
    if (start === end) {
      result.push(String(start));
    } else {
      result.push(`${start}->${end}`);
    }

    i++;
  }

  return result;
};