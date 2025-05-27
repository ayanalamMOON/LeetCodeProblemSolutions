package LEETCODE.Rgegular_Practice_Problems.Problem1;

import java.util.*;

class Solution {
    private static final int MOD = 1000000007;
    
    // Approach 1: 2D Dynamic Programming
    public int numWays(String[] words, String target) {
        int m = target.length();
        int n = words[0].length();
        
        if (m > n) return 0;
        
        // Precompute character frequencies at each position
        int[][] freq = new int[n][26];
        for (String word : words) {
            for (int i = 0; i < n; i++) {
                freq[i][word.charAt(i) - 'a']++;
            }
        }
        
        // DP table
        long[][] dp = new long[m + 1][n + 1];
        
        // Base case
        for (int j = 0; j <= n; j++) {
            dp[0][j] = 1;
        }
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                // Skip current position
                dp[i][j] = dp[i][j-1];
                
                // Use current position if character matches
                int charIndex = target.charAt(i-1) - 'a';
                if (freq[j-1][charIndex] > 0) {
                    dp[i][j] = (dp[i][j] + (dp[i-1][j-1] * freq[j-1][charIndex]) % MOD) % MOD;
                }
            }
        }
        
        return (int) dp[m][n];
    }
    
    // Approach 2: Space Optimized
    public int numWaysOptimized(String[] words, String target) {
        int m = target.length();
        int n = words[0].length();
        
        if (m > n) return 0;
        
        // Precompute frequencies
        int[][] freq = new int[n][26];
        for (String word : words) {
            for (int i = 0; i < n; i++) {
                freq[i][word.charAt(i) - 'a']++;
            }
        }
        
        // Space optimized DP
        long[] prev = new long[n + 1];
        long[] curr = new long[n + 1];
        Arrays.fill(prev, 1);
        
        for (int i = 1; i <= m; i++) {
            curr[0] = 0;
            for (int j = 1; j <= n; j++) {
                curr[j] = curr[j-1];
                
                int charIndex = target.charAt(i-1) - 'a';
                if (freq[j-1][charIndex] > 0) {
                    curr[j] = (curr[j] + (prev[j-1] * freq[j-1][charIndex]) % MOD) % MOD;
                }
            }
            System.arraycopy(curr, 0, prev, 0, n + 1);
            Arrays.fill(curr, 0);
        }
        
        return (int) prev[n];
    }
    
    // Approach 3: Memoized Recursion
    public int numWaysMemo(String[] words, String target) {
        int m = target.length();
        int n = words[0].length();
        
        if (m > n) return 0;
        
        // Precompute frequencies
        int[][] freq = new int[n][26];
        for (String word : words) {
            for (int i = 0; i < n; i++) {
                freq[i][word.charAt(i) - 'a']++;
            }
        }
        
        // Memoization
        Integer[][] memo = new Integer[m + 1][n + 1];
        return dfs(0, 0, target, freq, memo);
    }
    
    private int dfs(int targetIdx, int wordPos, String target, int[][] freq, Integer[][] memo) {
        int m = target.length();
        int n = freq.length;
        
        if (targetIdx == m) return 1;
        if (wordPos == n) return 0;
        if (n - wordPos < m - targetIdx) return 0;
        
        if (memo[targetIdx][wordPos] != null) {
            return memo[targetIdx][wordPos];
        }
        
        // Skip current position
        long result = dfs(targetIdx, wordPos + 1, target, freq, memo);
        
        // Use current position
        int charIndex = target.charAt(targetIdx) - 'a';
        if (freq[wordPos][charIndex] > 0) {
            result = (result + (1L * dfs(targetIdx + 1, wordPos + 1, target, freq, memo) * freq[wordPos][charIndex]) % MOD) % MOD;
        }
        
        return memo[targetIdx][wordPos] = (int) result;
    }
}

public class InJava {
    // Test function
    public static void runTests() {
        Solution solution = new Solution();
        
        // Test case 1
        String[] words1 = {"acca", "bbbb", "caca"};
        String target1 = "aba";
        assert solution.numWays(words1, target1) == 6;
        assert solution.numWaysOptimized(words1, target1) == 6;
        assert solution.numWaysMemo(words1, target1) == 6;
        
        // Test case 2
        String[] words2 = {"abba", "baab"};
        String target2 = "bab";
        assert solution.numWays(words2, target2) == 4;
        assert solution.numWaysOptimized(words2, target2) == 4;
        assert solution.numWaysMemo(words2, target2) == 4;
        
        System.out.println("All Java test cases passed!");
    }
    
    public static void demonstrateSolution(String[] words, String target) {
        Solution solution = new Solution();
        
        System.out.println("\n=== Java Analysis: words = " + Arrays.toString(words) + 
                          ", target = \"" + target + "\" ===");
        
        int n = words[0].length();
        int[][] freq = new int[n][26];
        for (String word : words) {
            for (int i = 0; i < n; i++) {
                freq[i][word.charAt(i) - 'a']++;
            }
        }
        
        System.out.println("Character frequency at each position:");
        for (int i = 0; i < n; i++) {
            System.out.print("Position " + i + ": ");
            for (int j = 0; j < 26; j++) {
                if (freq[i][j] > 0) {
                    System.out.print((char)('a' + j) + "=" + freq[i][j] + " ");
                }
            }
            System.out.println();
        }
        
        int result = solution.numWays(words, target);
        System.out.println("Number of ways: " + result);
    }
    
    public static void main(String[] args) {
        System.out.println("LeetCode 1639: Target String Formation - Java Solution");
        System.out.println("====================================================");
        
        runTests();
        
        String[] words1 = {"acca", "bbbb", "caca"};
        String target1 = "aba";
        demonstrateSolution(words1, target1);
        
        String[] words2 = {"abba", "baab"};
        String target2 = "bab";
        demonstrateSolution(words2, target2);
    }
}
