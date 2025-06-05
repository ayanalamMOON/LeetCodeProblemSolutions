/**
 * @file InJS.js
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

/**
 * Find lexicographically smallest equivalent string
 * @param {string} s1 - First equivalence string
 * @param {string} s2 - Second equivalence string
 * @param {string} baseStr - Base string to transform
 * @return {string} Lexicographically smallest equivalent string
 */
var smallestEquivalentString = function(s1, s2, baseStr) {
    // Initialize Union Find structure - each character maps to itself
    const parent = Array.from({length: 26}, (_, i) => i);
    
    /**
     * Find operation with path compression
     * @param {number} x - Character index (0-25 for 'a'-'z')
     * @return {number} Root representative of x's equivalence class
     */
    const find = (x) => {
        if (parent[x] !== x) {
            parent[x] = find(parent[x]); // Path compression
        }
        return parent[x];
    };
    
    /**
     * Union operation with lexicographical preference
     * @param {number} x - First character index
     * @param {number} y - Second character index
     */
    const unite = (x, y) => {
        const rootX = find(x), rootY = find(y);
        if (rootX !== rootY) {
            // Always make smaller character the root for lexicographical order
            if (rootX < rootY) {
                parent[rootY] = rootX;
            } else {
                parent[rootX] = rootY;
            }
        }
    };
    
    // Build equivalence relationships
    for (let i = 0; i < s1.length; i++) {
        unite(s1.charCodeAt(i) - 97, s2.charCodeAt(i) - 97); // 97 = 'a'.charCodeAt(0)
    }
    
    // Transform baseStr using equivalence mappings
    let result = '';
    for (const c of baseStr) {
        const charIdx = c.charCodeAt(0) - 97;
        const rootIdx = find(charIdx);
        result += String.fromCharCode(97 + rootIdx);
    }
    
    return result;
};

/**
 * Alternative implementation using class-based approach
 */
class UnionFindSolution {
    constructor() {
        this.parent = null;
    }
    
    /**
     * Find operation with path compression
     * @param {number} x - Character index
     * @return {number} Root representative
     */
    find(x) {
        if (this.parent[x] !== x) {
            this.parent[x] = this.find(this.parent[x]);
        }
        return this.parent[x];
    }
    
    /**
     * Union operation with lexicographical preference
     * @param {number} x - First character index
     * @param {number} y - Second character index
     */
    unite(x, y) {
        const rootX = this.find(x), rootY = this.find(y);
        if (rootX !== rootY) {
            if (rootX < rootY) {
                this.parent[rootY] = rootX;
            } else {
                this.parent[rootX] = rootY;
            }
        }
    }
    
    /**
     * Main solution method
     * @param {string} s1 - First equivalence string
     * @param {string} s2 - Second equivalence string
     * @param {string} baseStr - Base string to transform
     * @return {string} Result string
     */
    smallestEquivalentString(s1, s2, baseStr) {
        // Initialize parent array
        this.parent = Array.from({length: 26}, (_, i) => i);
        
        // Build equivalence relationships
        for (let i = 0; i < s1.length; i++) {
            this.unite(s1.charCodeAt(i) - 97, s2.charCodeAt(i) - 97);
        }
        
        // Transform baseStr
        return baseStr
            .split('')
            .map(c => String.fromCharCode(97 + this.find(c.charCodeAt(0) - 97)))
            .join('');
    }
}

/**
 * Test driver function
 */
function runTests() {
    console.log("Testing Function-based approach:");
    
    // Test Case 1
    const result1 = smallestEquivalentString("parker", "morris", "parser");
    console.log(`Test 1: ${result1}`); // Expected: "makkek"
    
    // Test Case 2
    const result2 = smallestEquivalentString("hello", "world", "hold");
    console.log(`Test 2: ${result2}`); // Expected: "hdld"
    
    // Test Case 3
    const result3 = smallestEquivalentString("leetcode", "programs", "sourcecode");
    console.log(`Test 3: ${result3}`); // Expected: "aauaaaaada"
    
    // Edge Case: No equivalences
    const result4 = smallestEquivalentString("aa", "aa", "abc");
    console.log(`Test 4: ${result4}`); // Expected: "abc"
    
    console.log("\nTesting Class-based approach:");
    const solution = new UnionFindSolution();
    
    // Test Case 1
    const classResult1 = solution.smallestEquivalentString("parker", "morris", "parser");
    console.log(`Class Test 1: ${classResult1}`); // Expected: "makkek"
    
    // Test Case 2
    const classResult2 = solution.smallestEquivalentString("hello", "world", "hold");
    console.log(`Class Test 2: ${classResult2}`); // Expected: "hdld"
    
    // Performance and edge case tests
    const testCases = [
        // All characters map to 'a'
        ["abc", "aaa", "xyz", "aaa"],
        // Single character
        ["a", "b", "c", "a"],
        // Empty base string
        ["ab", "cd", "", ""],
        // Long transitive chain
        ["abcdefg", "bcdefgh", "ghijklm", "aaaaaaa"],
    ];
    
    console.log("\nEdge case tests:");
    testCases.forEach(([s1, s2, baseStr, expected], i) => {
        const result = smallestEquivalentString(s1, s2, baseStr);
        console.log(`Edge Test ${i + 1}: ${result} (expected: ${expected})`);
        console.assert(result === expected, `Test ${i + 1} failed`);
    });
    
    console.log("All tests completed!");
}

// Run tests if this file is executed directly
if (typeof require !== 'undefined' && require.main === module) {
    runTests();
}

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        smallestEquivalentString,
        UnionFindSolution
    };
}
