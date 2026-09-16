# """
# Day 18 - Valid Parentheses
# Link: https://leetcode.com/problems/valid-parentheses/

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
    bool isValid(string s) {

      unordered_map<char, char> mp = {{')', '('}, {']', '['}, {'}', '{'}};
      stack<char> st;

      for(auto c : s){
        if(mp.find(c) == mp.end()){
            st.push(c);
        } else if(!st.empty() && mp[c] == st.top()){
            st.pop();
        } else{
            return false;
        }
      }

      return st.empty();         
    }
};