# """
# Day 20 - Daily Temperatures
# Link: https://leetcode.com/problems/daily-temperatures/

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
    vector<int> dailyTemperatures(vector<int>& t) {
        vector<int> ans(t.size(), 0);
        stack<int> st;

        for(int i = 0; i < t.size(); i++) {

            while(!st.empty() && t[i] > t[st.top()]) {
                ans[st.top()] = i - st.top();
                st.pop();
            }

            st.push(i);
        }

        return ans;
    }
};