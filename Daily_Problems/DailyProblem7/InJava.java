/**
 * @file InJava.java
 * @brief LeetCode 1061: Lexicographically Smallest Equivalent String
 * @author LeetCode Problem Solutions
 * @date 2024
 * 
 * Problem: Given two strings s1 and s2 of same length and a string baseStr,
 * find the lexicographically smallest equivalent string of baseStr using
 * character equivalence relationships from s1 and s2.
 * 
 * Approach: Union Find with Path Compression
 * - Use Union Find to manage character equivalence classes
 * - Always make lexicographically smaller character the root
 * - Apply path compression for optimal performance
 * 
 * Time Complexity: O(α(26) × (|s1| + |baseStr|)) ≈ O(|s1| + |baseStr|)
 * Space Complexity: O(26) = O(1)
 */

class Solution {
    private int[] parent;
    
    /**
     * Find operation with path compression
     * @param x Character index (0-25 for 'a'-'z')
     * @return Root representative of x's equivalence class
     */
    private int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]); // Path compression
        }
        return parent[x];
    }
    
    /**
     * Union operation with lexicographical preference
     * @param x First character index
     * @param y Second character index
     */
    private void unite(int x, int y) {
        int rootX = find(x), rootY = find(y);
        if (rootX != rootY) {
            // Always make smaller character the root for lexicographical order
            if (rootX < rootY) {
                parent[rootY] = rootX;
            } else {
                parent[rootX] = rootY;
            }
        }
    }
    
    /**
     * Find lexicographically smallest equivalent string
     * @param s1 First equivalence string
     * @param s2 Second equivalence string  
     * @param baseStr Base string to transform
     * @return Lexicographically smallest equivalent string
     */
    public String smallestEquivalentString(String s1, String s2, String baseStr) {
        // Initialize Union Find structure
        parent = new int[26];
        for (int i = 0; i < 26; i++) {
            parent[i] = i;
        }
        
        // Build equivalence relationships
        for (int i = 0; i < s1.length(); i++) {
            unite(s1.charAt(i) - 'a', s2.charAt(i) - 'a');
        }
        
        // Transform baseStr using equivalence mappings
        StringBuilder result = new StringBuilder(baseStr.length());
        for (char c : baseStr.toCharArray()) {
            result.append((char)('a' + find(c - 'a')));
        }
        
        return result.toString();
    }
    
    /**
     * Test driver method
     */
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Test Case 1
        String s1_1 = "parker", s2_1 = "morris", baseStr_1 = "parser";
        System.out.println("Test 1: " + solution.smallestEquivalentString(s1_1, s2_1, baseStr_1));
        // Expected: "makkek"
        
        // Test Case 2
        String s1_2 = "hello", s2_2 = "world", baseStr_2 = "hold";
        System.out.println("Test 2: " + solution.smallestEquivalentString(s1_2, s2_2, baseStr_2));
        // Expected: "hdld"
        
        // Test Case 3
        String s1_3 = "leetcode", s2_3 = "programs", baseStr_3 = "sourcecode";
        System.out.println("Test 3: " + solution.smallestEquivalentString(s1_3, s2_3, baseStr_3));
        // Expected: "aauaaaaada"
        
        // Edge Case: No equivalences
        String s1_4 = "aa", s2_4 = "aa", baseStr_4 = "abc";
        System.out.println("Test 4: " + solution.smallestEquivalentString(s1_4, s2_4, baseStr_4));
        // Expected: "abc"
    }
}
