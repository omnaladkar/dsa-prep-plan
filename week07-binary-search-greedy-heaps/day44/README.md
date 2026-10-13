<!-- # Day 44 - Search in Rotated Sorted Array (#33)

**LeetCode:** [search-in-rotated-sorted-array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

## Notes

**Pattern Trigger:** modified binary search

**Time spent:** 

**Approach:**
-

**Code:**
- See [solution.py](solution.py)

**Mistakes / Gotchas:**
- -->
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;

        while(left <= right) {
            int mid = left + (right - left) / 2;

            if(nums[mid] == target) {
                return mid;
            }

            // Left half is sorted
            if(nums[left] <= nums[mid]) {
                if(nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
            else {
                if(nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }

        return -1;
    }
};