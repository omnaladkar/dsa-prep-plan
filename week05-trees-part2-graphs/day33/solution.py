# """
# Day 33 - Course Schedule II
# Link: https://leetcode.com/problems/course-schedule-ii/

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
    vector<int> findOrder(int nC, vector<vector<int>>& pq) {
        vector<vector<int>> graph(nC);
        vector<int> inDegree(nC, 0);
        vector<int> ans;

        for(auto i : pq){
            int b = i[1];
            int a = i[0];

            graph[b].push_back(a);
            inDegree[a]++;
        }

        queue<int> q;

        int count = 0;

        for(int i = 0; i < nC; i++){
            if(inDegree[i] == 0){
                q.push(i);
            }
        }

        while(!q.empty()){
            int top = q.front();
            q.pop();

            ans.push_back(top);   // add when processed
            count++;

            for(int nex : graph[top]){
                
                inDegree[nex]--;

                if(inDegree[nex] == 0){
                    q.push(nex);
                }
            }
        }

        if(count == nC)
            return ans;

        return {};
    }
};