"""
Day 8 - Valid Palindrome
Link: https://leetcode.com/problems/valid-palindrome/

Pattern Trigger:
    [Write your pattern trigger here after solving]

Approach:
    - [Write your approach here]

Time Complexity:  O(?)
Space Complexity: O(?)
"""


class Solution:
    def methodName(self, params):
        pass


# ---------- Test Cases ----------
if __name__ == "__main__":
    sol = Solution()
    # Add test cases here
    # assert sol.methodName(input) == expected
    # print("All tests passed!")

class Solution {
public:
    bool isPalindrome(string s) {
        string p;

        for(auto i:s){
            if(isalnum(i))
             p += tolower(i);
             
        }

        for(int i=0;i<p.size();i++){
            if(p[i] != p[p.size()-i-1]){
            return false;
            }
        }

        return true;
    }
};