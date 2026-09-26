# """
# Day 34 - Number of Provinces
# Link: https://leetcode.com/problems/number-of-provinces/

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

    void dfs(int node, vector<vector<int>>& isConnected, vector<bool>& visited){
        visited[node] = true;
        int n = isConnected.size();

        for(int i=0;i<n ; i++){
            if(isConnected[node][i] == 1 && !visited[i]){
                dfs(i, isConnected, visited);
            }
        }
    }
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        vector<bool> visited(n, false);

        int provinces = 0;

        for(int i=0;i<n;i++){
            if(!visited[i]){
                dfs(i, isConnected, visited);
                provinces++;
            }

        }

        return provinces;
    }
};