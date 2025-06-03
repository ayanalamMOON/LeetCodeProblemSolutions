#include <vector>
#include <unordered_set>
#include <queue>
#include <iostream>
#include <cassert>

using namespace std;

class Solution {
public:
    int maxCandies(vector<int>& status, vector<int>& candies, vector<vector<int>>& keys, 
                   vector<vector<int>>& containedBoxes, vector<int>& initialBoxes) {
        // Track state
        unordered_set<int> availableBoxes(initialBoxes.begin(), initialBoxes.end());
        unordered_set<int> availableKeys;
        unordered_set<int> openedBoxes;
        queue<int> toProcess;
        int totalCandies = 0;
        
        // Add initially openable boxes to queue
        for (int box : initialBoxes) {
            if (status[box] == 1) {
                toProcess.push(box);
            }
        }
        
        // BFS to process all openable boxes
        while (!toProcess.empty()) {
            int currentBox = toProcess.front();
            toProcess.pop();
            
            // Skip if already opened
            if (openedBoxes.count(currentBox)) {
                continue;
            }
            
            // Open the box and collect candies
            openedBoxes.insert(currentBox);
            totalCandies += candies[currentBox];
            
            // Collect all keys from this box
            for (int key : keys[currentBox]) {
                availableKeys.insert(key);
            }
            
            // Collect all contained boxes
            for (int box : containedBoxes[currentBox]) {
                availableBoxes.insert(box);
            }
            
            // Check all available boxes to see if any can now be opened
            for (int box : availableBoxes) {
                if (!openedBoxes.count(box)) {
                    // Can open if box is initially open OR we have the key
                    if (status[box] == 1 || availableKeys.count(box)) {
                        toProcess.push(box);
                    }
                }
            }
        }
        
        return totalCandies;
    }
};

// Test function
void testSolution() {
    Solution solution;
    
    // Test Case 1
    vector<int> status1 = {1, 0, 1, 0};
    vector<int> candies1 = {7, 5, 4, 100};
    vector<vector<int>> keys1 = {{}, {}, {1}, {}};
    vector<vector<int>> containedBoxes1 = {{1, 2}, {3}, {}, {}};
    vector<int> initialBoxes1 = {0};
    
    int result1 = solution.maxCandies(status1, candies1, keys1, containedBoxes1, initialBoxes1);
    assert(result1 == 16);
    cout << "Test 1 passed: " << result1 << endl;
    
    // Test Case 2
    vector<int> status2 = {1, 0, 0, 0, 0, 0};
    vector<int> candies2 = {1, 1, 1, 1, 1, 1};
    vector<vector<int>> keys2 = {{1, 2, 3, 4, 5}, {}, {}, {}, {}, {}};
    vector<vector<int>> containedBoxes2 = {{1, 2, 3, 4, 5}, {}, {}, {}, {}, {}};
    vector<int> initialBoxes2 = {0};
    
    int result2 = solution.maxCandies(status2, candies2, keys2, containedBoxes2, initialBoxes2);
    assert(result2 == 6);
    cout << "Test 2 passed: " << result2 << endl;
    
    // Test Case 3: Edge case - no initial boxes
    vector<int> status3 = {1, 1, 1};
    vector<int> candies3 = {1, 2, 3};
    vector<vector<int>> keys3 = {{}, {}, {}};
    vector<vector<int>> containedBoxes3 = {{}, {}, {}};
    vector<int> initialBoxes3 = {};
    
    int result3 = solution.maxCandies(status3, candies3, keys3, containedBoxes3, initialBoxes3);
    assert(result3 == 0);
    cout << "Test 3 passed: " << result3 << endl;
    
    // Test Case 4: All boxes closed, no keys
    vector<int> status4 = {0, 0, 0};
    vector<int> candies4 = {1, 2, 3};
    vector<vector<int>> keys4 = {{}, {}, {}};
    vector<vector<int>> containedBoxes4 = {{}, {}, {}};
    vector<int> initialBoxes4 = {0, 1, 2};
    
    int result4 = solution.maxCandies(status4, candies4, keys4, containedBoxes4, initialBoxes4);
    assert(result4 == 0);
    cout << "Test 4 passed: " << result4 << endl;
    
    cout << "All tests passed!" << endl;
}

int main() {
    testSolution();
    return 0;
}

/*
Time Complexity: O(n) where n is the number of boxes
- Each box is processed at most once
- Set operations are O(1) on average

Space Complexity: O(n)
- Sets to track available boxes, keys, and opened boxes
- Queue for BFS traversal

Algorithm:
1. Initialize state tracking with sets and queue
2. Add initially openable boxes (available + open) to queue
3. BFS: For each box in queue:
   - Skip if already opened
   - Open box: collect candies, keys, contained boxes
   - Check all available boxes for newly openable ones
4. Continue until queue is empty
5. Return total candies collected

Key Insights:
- Use BFS to ensure we process boxes as soon as they become available
- Track three types of state: available boxes, collected keys, opened boxes
- A box can be opened if we have it AND (it's initially open OR we have its key)
- Order of opening doesn't affect total candies, only reachability matters
*/
