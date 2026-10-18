# Day 45 - Find Minimum in Rotated Sorted Array (#153)

**LeetCode:** [find-minimum-in-rotated-sorted-array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

## Notes

**Pattern Trigger:** binary search on rotation point

**Time spent:** 

**Approach:**
-

**Code:**
- See [solution.py](solution.py)

**Mistakes / Gotchas:**
-
class Solution {
public:
    int findMin(vector<int>& nums) {
        int n = nums.size();

        int left  = 0;
        int right = n-1;

        while(left<right){
            int mid = left + (right - left)/2;

            if(nums[mid] >  nums[right]){
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return nums[left];
    }
};