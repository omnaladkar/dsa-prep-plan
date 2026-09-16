<!-- # Day 19 - Min Stack (#155)

**LeetCode:** [min-stack](https://leetcode.com/problems/min-stack/)

## Notes

**Pattern Trigger:** stack tracking running min

**Time spent:** 

**Approach:**
-

**Code:**
- See [solution.py](solution.py)

**Mistakes / Gotchas:**
- -->
class MinStack {
public:
    stack<int> st;
    stack<int> mn;

    MinStack() {
        
    }
    
    void push(int value) {
        st.push(value);

        if (mn.empty() || value <= mn.top()) {
            mn.push(value);
        } else {
            mn.push(mn.top());
        }
    }
    
    void pop() {
        st.pop();
        mn.pop();
    }
    
    int top() {
        return st.top();
    }
    
    int getMin() {
        return mn.top();
    }
};