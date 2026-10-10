# """
# Day 41 - Partition Equal Subset Sum
# Link: https://leetcode.com/problems/partition-equal-subset-sum/

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
    bool canPartition(vector<int>& nums) {
        // first thing it is saying both subset should be equal it means total
        // guy should be divide by 2
        int totalsum = 0;

        for (auto i : nums) {
            totalsum += i;
        }

        if (totalsum % 2 != 0) {
            return false;
        }

        int p = totalsum / 2;

        vector<int> dp(p + 1, 0);
        dp[0] = 1;

        for (int i = 0; i < nums.size(); i++) {
            for (int j = p; j >= nums[i]; j--) {
                if (dp[j - nums[i]]) {
                    dp[j] = 1;
                }
            }
        }

        return dp[p];
    }
};