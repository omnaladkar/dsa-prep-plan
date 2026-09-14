# """
# Day 17 - Merge Two Sorted Lists
# Link: https://leetcode.com/problems/merge-two-sorted-lists/

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
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* secon = new ListNode(0);
        ListNode* curr = secon;

        while(list1 && list2){
            if(list1->val > list2->val){
                curr->next = list2;
                list2 = list2->next;
            } else  {
                curr->next = list1;
                list1 = list1->next;
            }
            curr = curr->next;
        } 

        curr->next = list1 ? list1 : list2;
       ListNode* ans = secon->next;

       delete secon;
       return ans;


    }
};