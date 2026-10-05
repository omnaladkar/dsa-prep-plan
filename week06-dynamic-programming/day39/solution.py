# """
# Day 39 - Coin Change
# Link: https://leetcode.com/problems/coin-change/

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
    int coinChange(vector<int>& coins, int amount) {
        sort(coins.begin(), coins.end());

        map<int, int> mp;
        mp[0] = 0;

        for(int i = 1; i <= amount; i++) {
            int ans = INT_MAX;

            for(int j = coins.size() - 1; j >= 0; j--) {
                if(coins[j] <= i && mp.count(i - coins[j])) {
                    ans = min(ans, mp[i - coins[j]] + 1);
                }
            }

            if(ans != INT_MAX)
                mp[i] = ans;
        }

        if(mp.count(amount))
            return mp[amount];

        return -1;
    }
};