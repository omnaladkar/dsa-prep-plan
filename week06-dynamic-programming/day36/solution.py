# """
# Day 36 - Climbing Stairs
# Link: https://leetcode.com/problems/climbing-stairs/
# # 
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
    int climbStairs(int n) {
        vector<int> dp(n+1, -1);

        dp[0] = 1;
        dp[1]  = 1;
      

        for(int i=2;i<=n;i++){
         dp[i] = dp[i-1] + dp[i-2];
        }

        return dp[n];
    }
};