"""
Day 6 - Subarray Sum Equals K
Link: https://leetcode.com/problems/subarray-sum-equals-k/

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
    int subarraySum(vector<int>& nums, int k) {
       int n = nums.size();
        int count = 0;

        for(int i=0;i<n;i++){
            int sum = 0;
            for(int j=i;j<n;j++){
               sum += nums[j];
               if(sum == k){
                count++;
               } 
            }
        }

        return count;
    }
};