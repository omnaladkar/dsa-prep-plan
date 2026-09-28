# """
# Day 37 - House Robber
# Link: https://leetcode.com/problems/house-robber/

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
    int rob(vector<int>& nums) {
        int n = nums.size();

        if(n == 1) return nums[0];

        vector<int> dp(n+1, 0);
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);

        for(int i=2;i<n;i++){
            dp[i] = max(dp[i-1], nums[i]+dp[i-2]);
        }

        return dp[n-1];
    }
};