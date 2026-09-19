# """
# Day 27 - Lowest Common Ancestor of a BST
# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

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
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {

        if(root->val > p->val && root->val > q->val){
            return lowestCommonAncestor(root->left, p, q);
        } else if (root->val < p->val && root->val < q->val){
            return lowestCommonAncestor(root->right, p, q);
        } else {
            return root;
        }

    }
};
