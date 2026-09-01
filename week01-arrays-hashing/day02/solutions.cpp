# """
# Day 2 - Best Time to Buy and Sell Stock
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Pattern Trigger:
#     [Write your pattern trigger here after solving]

# Approach:
#     - [Write your approach here]

# Time Complexity:  O(?)
# Space Complexity: O(?)
"""


# class Solution:
#     def methodName(self, params):
#         pass


# ---------- Test Cases ----------
# if __name__ == "__main__":
#     sol = Solution()
#     # Add test cases here
#     # assert sol.methodName(input) == expected
#     # print("All tests passed!")

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minPrice = prices[0];
        int ans = 0;

        for(int i=1;i<prices.size();i++){
            minPrice = min(prices[i], minPrice);
            ans = max(ans, prices[i] - minPrice);
        }

        return ans;
    }
};