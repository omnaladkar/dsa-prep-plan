/*
Day 1 - Subarray Sum Equals K (LeetCode #560)
Link: https://leetcode.com/problems/subarray-sum-equals-k/

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
    int subarraySum(vector<int>& nums, int k) {
        // map all the items for nums in map key count
        // var count  = 0
        // you can run the nums for loop and do check the the map (k - nums[i]) that is value present in map then just the frequecy -- or if the subtraction cooming zero then also add count++
        //end retunr count

         unordered_map<int, int> mp;
        int sum = 0;
        int count = 0;

        mp[0] = 1;

        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];

            if (mp.find(sum - k) != mp.end()) {
                count += mp[sum - k];
            }

            mp[sum]++;
        }

        return count;
    }
};