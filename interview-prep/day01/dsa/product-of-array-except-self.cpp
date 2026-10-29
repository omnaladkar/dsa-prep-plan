/*
Day 1 - Product of Array Except Self (LeetCode #238)
Link: https://leetcode.com/problems/product-of-array-except-self/

Pattern Trigger: (fill in after solving)
Brute force + complexity:
Optimal approach:
Time Complexity:  O(?)
Space Complexity: O(?)
Edge cases tested:
Time taken: __ min | Solved without help: yes / no
*/

#include <bits/stdc++.h>
using namespace std;

// Paste / write your Solution class here


// int main() {
//     // Add 2-3 test cases here, including edge cases
//     return 0;
// }

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