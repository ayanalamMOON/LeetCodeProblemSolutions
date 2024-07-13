class Solution {
public:
    vector<int> survivedRobotsHealths(vector<int>& positions, vector<int>& healths, string directions) {
        int n = positions.size();
        vector<int> index(n);
        vector<int> result(n, -1);  // -1 means the robot is removed
        
        // Initialize index with 0 to n-1
        for (int i = 0; i < n; ++i) {
            index[i] = i;
        }
        
        // Sort indices based on the positions
        sort(index.begin(), index.end(), [&](int a, int b) {
            return positions[a] < positions[b];
        });
        
        stack<int> st; // Stack to store indices of robots moving right ('R')
        
        for (int i : index) {
            if (directions[i] == 'R') {
                st.push(i);
            } else { // directions[i] == 'L'
                while (!st.empty() && healths[i] > 0) {
                    int j = st.top();
                    if (healths[j] > healths[i]) {
                        healths[j] -= 1;
                        healths[i] = 0;
                    } else if (healths[j] < healths[i]) {
                        st.pop();
                        healths[i] -= 1;
                    } else {
                        st.pop();
                        healths[j] = 0;
                        healths[i] = 0;
                    }
                }
                if (healths[i] > 0) {
                    result[i] = healths[i];
                }
            }
        }
        
        // Add remaining robots in the stack to the result
        while (!st.empty()) {
            int j = st.top();
            st.pop();
            result[j] = healths[j];
        }
        
        // Collect the healths of surviving robots in the original order
        vector<int> survivors;
        for (int i = 0; i < n; ++i) {
            if (result[i] != -1) {
                survivors.push_back(result[i]);
            }
        }
        
        return survivors;
    }
};