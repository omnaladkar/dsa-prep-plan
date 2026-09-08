# """
# Day 10 - Container With Most Water
# Link: https://leetcode.com/problems/container-with-most-water/

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
    int maxArea(vector<int>& height) {
        // int sum = 0;
        // for(int i=0;i<height.size();i++){
        //     int j = i+1;
        //     while(j < height.size()){
        //         int t = min(height[i], height[j]);
        //         sum = max(sum, t*(j-i));
        //         j++;
        //     }
        // }

        // return sum;
        int n = height.size();
        int left = 0;
        int right = n-1;
    
        int sum = 0;
        while(left < right){
            int mins = min(height[left], height[right]);
            sum = max(sum, mins*(right - left));
            if(height[left] > height[right]){
                right--;
            } else{
                left++;
            }
        }

        return sum;
    }
};