# """
# Day 26 - Validate Binary Search Tree
# Link: https://leetcode.com/problems/validate-binary-search-tree/

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


    void findInorder(TreeNode* root, vector<int>& ans){
        if(!root){
            return;
        }

        findInorder(root->left, ans);
        ans.push_back(root->val);
        findInorder(root->right, ans);
    }

    bool isValidBST(TreeNode* root) {
        if(!root){
            return true;
        }

        vector<int> ans;

        findInorder(root, ans);

        for(int i=1; i<ans.size(); i++){
            if(ans[i-1] >= ans[i]){
                return false;
            }
        }

        return true;
    }
};