# """
# Day 38 - Longest Increasing Subsequence
# Link: https://leetcode.com/problems/longest-increasing-subsequence/

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
    int lengthOfLIS(vector<int>& nums) {
        // we need to create a dp
        // we have to create two for loop 
        // start with i=0
        // second with j = i+1;
        // and in between we have to check the i+1 > i then we will continue because there is no use
        // then we will check for each element and then next two are greater and we have to check that element should not be equeal and we ahve o the mnimum of the two element 
         int n = nums.size();
    vector<int> dp(n, 1); 


    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
  
            if (nums[j] <= nums[i]) continue;

            dp[j] = max(dp[j], dp[i] + 1);
        }
    }

    // maximum LIS value
    return *max_element(dp.begin(), dp.end());
    }
};
