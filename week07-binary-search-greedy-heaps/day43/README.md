<!-- # Day 43 - Binary Search (#704)

**LeetCode:** [binary-search](https://leetcode.com/problems/binary-search/)

## Notes

**Pattern Trigger:** template refresh

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
        int n = nums.size();

        int left = 0;
        int right = n - 1;

        while(left <= right) {
            int mid = (left + right) / 2;

            if(nums[mid] > target) {
                right = mid - 1;
            } 
            else if(nums[mid] < target) {
                left = mid + 1;
            } 
            else {
                return mid;
            }
        }

        return -1;
    }
};
