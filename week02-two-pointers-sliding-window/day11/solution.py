# """
# Day 11 - Longest Substring Without Repeating Characters
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

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
    int lengthOfLongestSubstring(string s) {
        

        // int ans = 1;

        // int sl = s.size();
        // if(sl == 0){
        //     return 0;
        // }

        // for(int i=0;i<sl;i++){
        //     int j = i+1;
        //     set<char> st;
        //     st.insert(s[i]);
        //     while(i < j && j<sl){
        //         if(st.count(s[j])){
        //             ans = max(ans, (int)st.size());
        //             break;
        //         }
        //         st.insert(s[j]);
        //         ans = max(ans, (int)st.size());
        //         j++;

        //     }
        // }

        // return ans;

        int ans = 0;
        int i = 0, j = 0;

        set<char> st;

        while(j < s.size()) {
            if(st.count(s[j])) {
                st.erase(s[i]);
                i++;
            }
            else {
                st.insert(s[j]);
                ans = max(ans, (int)st.size());
                j++;
            }
        }

        return ans;
    }
};