#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <cassert>
using namespace std;

class Solution {
private:
    static const int MOD = 1000000007;
    
public:
    // Approach 1: 2D Dynamic Programming with Character Frequency
    int numWays(vector<string>& words, string target) {
        int m = target.length();
        int n = words[0].length();
        
        // Early termination: if target is longer than word length, impossible
        if (m > n) return 0;
        
        // Step 1: Precompute character frequencies at each position
        vector<vector<int>> freq(n, vector<int>(26, 0));
        for (const string& word : words) {
            for (int i = 0; i < n; i++) {
                freq[i][word[i] - 'a']++;
            }
        }
        
        // Step 2: DP table - dp[i][j] = ways to form first i chars using first j positions
        vector<vector<long long>> dp(m + 1, vector<long long>(n + 1, 0));
        
        // Base case: empty target can be formed in 1 way
        for (int j = 0; j <= n; j++) {
            dp[0][j] = 1;
        }
        
        // Fill DP table
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                // Option 1: Skip current position
                dp[i][j] = dp[i][j-1];
                
                // Option 2: Use current position if character matches
                char targetChar = target[i-1];
                int charIndex = targetChar - 'a';
                if (freq[j-1][charIndex] > 0) {
                    dp[i][j] = (dp[i][j] + (dp[i-1][j-1] * freq[j-1][charIndex]) % MOD) % MOD;
                }
            }
        }
        
        return dp[m][n];
    }
    
    // Approach 2: Space Optimized 1D DP
    int numWaysOptimized(vector<string>& words, string target) {
        int m = target.length();
        int n = words[0].length();
        
        if (m > n) return 0;
        
        // Precompute frequencies
        vector<vector<int>> freq(n, vector<int>(26, 0));
        for (const string& word : words) {
            for (int i = 0; i < n; i++) {
                freq[i][word[i] - 'a']++;
            }
        }
        
        // Space optimized DP - only need current and previous row
        vector<long long> prev(n + 1, 1), curr(n + 1, 0);
        
        for (int i = 1; i <= m; i++) {
            curr[0] = 0; // Can't form non-empty target with 0 positions
            for (int j = 1; j <= n; j++) {
                curr[j] = curr[j-1];
                
                char targetChar = target[i-1];
                int charIndex = targetChar - 'a';
                if (freq[j-1][charIndex] > 0) {
                    curr[j] = (curr[j] + (prev[j-1] * freq[j-1][charIndex]) % MOD) % MOD;
                }
            }
            prev = curr;
            fill(curr.begin(), curr.end(), 0);
        }
        
        return prev[n];
    }
    
    // Approach 3: Memoized Recursion (Top-Down DP)
    int numWaysMemo(vector<string>& words, string target) {
        int m = target.length();
        int n = words[0].length();
        
        if (m > n) return 0;
        
        // Precompute frequencies
        vector<vector<int>> freq(n, vector<int>(26, 0));
        for (const string& word : words) {
            for (int i = 0; i < n; i++) {
                freq[i][word[i] - 'a']++;
            }
        }
        
        // Memoization table
        vector<vector<int>> memo(m + 1, vector<int>(n + 1, -1));
        
        function<int(int, int)> dfs = [&](int targetIdx, int wordPos) -> int {
            // Base cases
            if (targetIdx == m) return 1; // Formed complete target
            if (wordPos == n) return 0;   // No more positions available
            if (n - wordPos < m - targetIdx) return 0; // Not enough positions left
            
            if (memo[targetIdx][wordPos] != -1) {
                return memo[targetIdx][wordPos];
            }
            
            // Option 1: Skip current position
            long long result = dfs(targetIdx, wordPos + 1);
            
            // Option 2: Use current position
            char targetChar = target[targetIdx];
            int charIndex = targetChar - 'a';
            if (freq[wordPos][charIndex] > 0) {
                result = (result + (1LL * dfs(targetIdx + 1, wordPos + 1) * freq[wordPos][charIndex]) % MOD) % MOD;
            }
            
            return memo[targetIdx][wordPos] = result;
        };
        
        return dfs(0, 0);
    }
};

// Test functions
void runTests() {
    Solution solution;
    
    // Test case 1
    vector<string> words1 = {"acca", "bbbb", "caca"};
    string target1 = "aba";
    assert(solution.numWays(words1, target1) == 6);
    assert(solution.numWaysOptimized(words1, target1) == 6);
    assert(solution.numWaysMemo(words1, target1) == 6);
    
    // Test case 2
    vector<string> words2 = {"abba", "baab"};
    string target2 = "bab";
    assert(solution.numWays(words2, target2) == 4);
    assert(solution.numWaysOptimized(words2, target2) == 4);
    assert(solution.numWaysMemo(words2, target2) == 4);
    
    // Edge cases
    vector<string> words3 = {"a", "b"};
    string target3 = "ab";
    assert(solution.numWays(words3, target3) == 1);
    
    vector<string> words4 = {"abc"};
    string target4 = "abcd";
    assert(solution.numWays(words4, target4) == 0); // Target longer than word
    
    cout << "All test cases passed!" << endl;
}

void demonstrateSolution(vector<string>& words, string target) {
    Solution solution;
    
    cout << "\n=== Analyzing: words = [";
    for (int i = 0; i < words.size(); i++) {
        cout << "\"" << words[i] << "\"";
        if (i < words.size() - 1) cout << ", ";
    }
    cout << "], target = \"" << target << "\" ===" << endl;
    
    // Show character frequency table
    int n = words[0].length();
    vector<vector<int>> freq(n, vector<int>(26, 0));
    for (const string& word : words) {
        for (int i = 0; i < n; i++) {
            freq[i][word[i] - 'a']++;
        }
    }
    
    cout << "Character frequency at each position:" << endl;
    for (int i = 0; i < n; i++) {
        cout << "Position " << i << ": ";
        for (int j = 0; j < 26; j++) {
            if (freq[i][j] > 0) {
                cout << (char)('a' + j) << "=" << freq[i][j] << " ";
            }
        }
        cout << endl;
    }
    
    int result = solution.numWays(words, target);
    cout << "Number of ways to form \"" << target << "\": " << result << endl;
}

int main() {
    cout << "LeetCode 1639: Number of Ways to Form a Target String Given a Dictionary" << endl;
    cout << "=======================================================================" << endl;
    
    // Run tests
    runTests();
    
    // Demonstrate examples
    vector<string> words1 = {"acca", "bbbb", "caca"};
    string target1 = "aba";
    demonstrateSolution(words1, target1);
    
    vector<string> words2 = {"abba", "baab"};
    string target2 = "bab";
    demonstrateSolution(words2, target2);
    
    // Interactive mode
    cout << "\n=== Interactive Mode ===" << endl;
    cout << "Enter number of words: ";
    int numWords;
    cin >> numWords;
    
    vector<string> words(numWords);
    cout << "Enter " << numWords << " words:" << endl;
    for (int i = 0; i < numWords; i++) {
        cin >> words[i];
    }
    
    cout << "Enter target string: ";
    string target;
    cin >> target;
    
    Solution solution;
    int result = solution.numWays(words, target);
    cout << "Number of ways: " << result << endl;
    
    return 0;
}