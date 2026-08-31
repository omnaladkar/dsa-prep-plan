"""
Day 1 - Two Sum
Link: https://leetcode.com/problems/two-sum/

Pattern Trigger:
    [Write your pattern trigger here after solving]

Approach:
    - [Write your approach here]

Time Complexity:  O(?)
Space Complexity: O(?)
"""


# class Solution:
#     def methodName(self, params):
#         pass


# ---------- Test Cases ----------
// if __name__ == "__main__":
//     sol = Solution()
//     # Add test cases here
//     # assert sol.methodName(input) == expected
//     # print("All tests passed!")

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Use unordered_map for O(1) lookups instead of map O(log N)
        unordered_map<int, int> mp; 

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];

            // If complement exists in map, we found the pair!
            if (mp.find(complement) != mp.end()) {
                return {mp[complement], i};
            }

            // Otherwise, store current number and its index
            mp[nums[i]] = i;
        }

        return {}; // Return empty vector if no solution exists
    }
};
