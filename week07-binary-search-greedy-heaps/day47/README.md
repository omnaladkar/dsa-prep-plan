<!-- # Day 47 - Top K Frequent Elements (#347)

**LeetCode:** [top-k-frequent-elements](https://leetcode.com/problems/top-k-frequent-elements/)

## Notes

**Pattern Trigger:** heap + hashmap count

**Time spent:** 

**Approach:**
-

**Code:**
- See [solution.py](solution.py)

**Mistakes / Gotchas:**
- -->
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) 
    {
        vector<int>ans;
        map<int,int>mpp;
        for(int i=0;i<nums.size();i++)
        {
            mpp[nums[i]]++;
        }
        priority_queue<pair<int,int>>pq;
        for(auto it:mpp)
        {
            pq.push({it.second,it.first});
        }
        while(k>0)
        {
            ans.push_back(pq.top().second);
            pq.pop();
            k--;
        }
        return ans;
    }

};