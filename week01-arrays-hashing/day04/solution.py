"""
Day 4 - Product of Array Except Self
Link: https://leetcode.com/problems/product-of-array-except-self/

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
    vector<int> productExceptSelf(vector<int>& nums) {
       int prod = 1;
       int zeros = 0;
       
    int n = nums.size();
    vector<int> ans(n);
    for(int i=0;i<n;i++){
        if(nums[i] == 0){
           zeros++;
           continue;
        }
        
        prod = prod*nums[i];


    }

    if(zeros > 0){
        if(zeros > 0 && zeros > 1){
            
            for(int i=0;i<n;i++){
            
            ans[i] = 0;

        }
        return ans;

        }
        for(int i=0;i<n;i++){
            if(nums[i] == 0){
               ans[i] = prod; 
               continue;
            }
            ans[i] = 0;

        }
    } else {
      for(int i=0;i<n;i++){
           
            ans[i] = prod/nums[i];

        }  
    }

    return ans;
    }
};