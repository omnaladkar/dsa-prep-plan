# """
# Day 12 - Minimum Window Substring
# Link: https://leetcode.com/problems/minimum-window-substring/

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

    string minWindow(string s, string t) {

        if(t.size() == 0 || t.size() > s.size()) {
            return "";
        }

        map<char, int> mp;

        for(int i = 0; i < t.size(); i++) {
            mp[t[i]]++;
        }

        int i = 0;
        int count = t.size();

        int start = 0;
        int len = INT_MAX;

        for(int j = 0; j < s.size(); j++) {

           
            if(mp[s[j]] > 0) {
                count--;
            }

            mp[s[j]]--;

        
            while(count == 0) {

            
                if(j - i + 1 < len) {
                    len = j - i + 1;
                    start = i;
                }


                mp[s[i]]++;

                if(mp[s[i]] > 0) {
                    count++;
                }

                i++;
            }
        }

        if(len == INT_MAX) {
            return "";
        }

        return s.substr(start, len);
    }
};