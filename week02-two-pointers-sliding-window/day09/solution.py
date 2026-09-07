# """
# Day 9 - 3Sum
# Link: https://leetcode.com/problems/3sum/

# Pattern Trigger:
#     [Write your pattern trigger here after solving]

# Approach:
#     - [Write your approach here]

# Time Complexity:  O(?)
# Space Complexity: O(?)
# """


# class Solution:
#     def methodName(self, params):
#         pass


# # ---------- Test Cases ----------
# if __name__ == "__main__":
#     sol = Solution()
#     # Add test cases here
#     # assert sol.methodName(input) == expected
#     # print("All tests passed!")

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        vector<vector<int>> ans;

        map<int, int> mp;

        for (int i = 0; i < nums.size(); i++) {
            mp[nums[i]] = i;
        }

        for (int i = 0; i < nums.size(); i++) {

            if (i > 0 && nums[i] == nums[i - 1])
                continue;

            for (int j = i + 1; j < nums.size(); j++) {

                if (j > i + 1 && nums[j] == nums[j - 1])
                    continue;

                int sum = nums[i] + nums[j];
                int target = -sum;

                if (mp.find(target) != mp.end()) {

                    int k = mp[target];

                    if (k > j) {
                        ans.push_back({nums[i], nums[j], target});
                    }
                }
            }
        }

        return ans;
    }
};