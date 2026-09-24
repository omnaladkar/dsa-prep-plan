# """
# Day 32 - Course Schedule
# Link: https://leetcode.com/problems/course-schedule/

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
    bool dfs(int course, map<int, vector<int>>& mp, vector<int>& vis) {

        if (vis[course] == 1) {
            return false;   // cycle found
        }

        if (vis[course] == 2) {
            return true;    // already completed
        }

        vis[course] = 1;

        for (int next : mp[course]) {
            if (!dfs(next, mp, vis)) {
                return false;
            }
        }

        vis[course] = 2;

        return true;
    }

    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {

        map<int, vector<int>> mp;

        for (auto p : prerequisites) {
            mp[p[1]].push_back(p[0]);
        }

        vector<int> vis(numCourses, 0);

        for (int i = 0; i < numCourses; i++) {
            if (!dfs(i, mp, vis)) {
                return false;
            }
        }

        return true;
    }
};


// kanhs algo 

// So we need to create a graph and we need to create a inDegree as well so what are the things are dependent on that that eleemtent times it is dependen

class Solution {
public:
    bool canFinish(int nC, vector<vector<int>>& pq) {
        vector<vector<int>> graph(nC);
        vector<int> inDegree(nC, 0);

        for(auto i : pq){
            int b = i[1];
            int a = i[0];

            graph[b].push_back(a);
            inDegree[a]++;
        }

        queue<int> q;

        int count = 0;

        for(int i=0;i<nC;i++){

            if(inDegree[i] == 0){
                q.push(i);
            }
        }

        while(!q.empty()){
            int top = q.front();
            q.pop();
            count++;

            for(int nex : graph[top]){
                
                inDegree[nex]--;

                if(inDegree[nex] == 0){
                    q.push(nex);
                }
            }



        }


        return count == nC;
    }
};