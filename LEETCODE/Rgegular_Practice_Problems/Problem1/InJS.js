/**
 * @param {string[]} words
 * @param {string} target
 * @return {number}
 */

class Solution {
    // Approach 1: 2D Dynamic Programming
    numWays(words, target) {
        const MOD = 1000000007;
        const m = target.length;
        const n = words[0].length;
        
        if (m > n) return 0;
        
        // Precompute character frequencies at each position
        const freq = Array(n).fill().map(() => Array(26).fill(0));
        for (const word of words) {
            for (let i = 0; i < n; i++) {
                freq[i][word.charCodeAt(i) - 97]++; // 97 is 'a'.charCodeAt(0)
            }
        }
        
        // DP table
        const dp = Array(m + 1).fill().map(() => Array(n + 1).fill(0));
        
        // Base case
        for (let j = 0; j <= n; j++) {
            dp[0][j] = 1;
        }
        
        for (let i = 1; i <= m; i++) {
            for (let j = 1; j <= n; j++) {
                // Skip current position
                dp[i][j] = dp[i][j-1];
                
                // Use current position if character matches
                const charIndex = target.charCodeAt(i-1) - 97;
                if (freq[j-1][charIndex] > 0) {
                    dp[i][j] = (dp[i][j] + (dp[i-1][j-1] * freq[j-1][charIndex]) % MOD) % MOD;
                }
            }
        }
        
        return dp[m][n];
    }
    
    // Approach 2: Space Optimized
    numWaysOptimized(words, target) {
        const MOD = 1000000007;
        const m = target.length;
        const n = words[0].length;
        
        if (m > n) return 0;
        
        // Precompute frequencies
        const freq = Array(n).fill().map(() => Array(26).fill(0));
        for (const word of words) {
            for (let i = 0; i < n; i++) {
                freq[i][word.charCodeAt(i) - 97]++;
            }
        }
        
        // Space optimized DP
        let prev = Array(n + 1).fill(1);
        let curr = Array(n + 1).fill(0);
        
        for (let i = 1; i <= m; i++) {
            curr[0] = 0;
            for (let j = 1; j <= n; j++) {
                curr[j] = curr[j-1];
                
                const charIndex = target.charCodeAt(i-1) - 97;
                if (freq[j-1][charIndex] > 0) {
                    curr[j] = (curr[j] + (prev[j-1] * freq[j-1][charIndex]) % MOD) % MOD;
                }
            }
            [prev, curr] = [curr, Array(n + 1).fill(0)];
        }
        
        return prev[n];
    }
    
    // Approach 3: Memoized Recursion
    numWaysMemo(words, target) {
        const MOD = 1000000007;
        const m = target.length;
        const n = words[0].length;
        
        if (m > n) return 0;
        
        // Precompute frequencies
        const freq = Array(n).fill().map(() => Array(26).fill(0));
        for (const word of words) {
            for (let i = 0; i < n; i++) {
                freq[i][word.charCodeAt(i) - 97]++;
            }
        }
        
        // Memoization using Map for better performance
        const memo = new Map();
        
        const dfs = (targetIdx, wordPos) => {
            // Base cases
            if (targetIdx === m) return 1;
            if (wordPos === n) return 0;
            if (n - wordPos < m - targetIdx) return 0;
            
            const key = `${targetIdx},${wordPos}`;
            if (memo.has(key)) {
                return memo.get(key);
            }
            
            // Skip current position
            let result = dfs(targetIdx, wordPos + 1);
            
            // Use current position
            const charIndex = target.charCodeAt(targetIdx) - 97;
            if (freq[wordPos][charIndex] > 0) {
                result = (result + (dfs(targetIdx + 1, wordPos + 1) * freq[wordPos][charIndex]) % MOD) % MOD;
            }
            
            memo.set(key, result);
            return result;
        };
        
        return dfs(0, 0);
    }
    
    // Approach 4: Using ES6 Map for frequency counting
    numWaysES6(words, target) {
        const MOD = 1000000007;
        const m = target.length;
        const n = words[0].length;
        
        if (m > n) return 0;
        
        // Use Map for more JavaScript-like frequency counting
        const freq = Array(n).fill().map(() => new Map());
        for (const word of words) {
            for (let i = 0; i < n; i++) {
                const char = word[i];
                freq[i].set(char, (freq[i].get(char) || 0) + 1);
            }
        }
        
        const dp = Array(m + 1).fill().map(() => Array(n + 1).fill(0));
        
        // Base case
        for (let j = 0; j <= n; j++) {
            dp[0][j] = 1;
        }
        
        for (let i = 1; i <= m; i++) {
            for (let j = 1; j <= n; j++) {
                dp[i][j] = dp[i][j-1];
                
                const targetChar = target[i-1];
                const count = freq[j-1].get(targetChar) || 0;
                if (count > 0) {
                    dp[i][j] = (dp[i][j] + (dp[i-1][j-1] * count) % MOD) % MOD;
                }
            }
        }
        
        return dp[m][n];
    }
}

// Test function
function runTests() {
    const solution = new Solution();
    
    // Test case 1
    const words1 = ["acca", "bbbb", "caca"];
    const target1 = "aba";
    console.assert(solution.numWays(words1, target1) === 6, "Test case 1 failed");
    console.assert(solution.numWaysOptimized(words1, target1) === 6, "Test case 1 optimized failed");
    console.assert(solution.numWaysMemo(words1, target1) === 6, "Test case 1 memo failed");
    console.assert(solution.numWaysES6(words1, target1) === 6, "Test case 1 ES6 failed");
    
    // Test case 2
    const words2 = ["abba", "baab"];
    const target2 = "bab";
    console.assert(solution.numWays(words2, target2) === 4, "Test case 2 failed");
    console.assert(solution.numWaysOptimized(words2, target2) === 4, "Test case 2 optimized failed");
    console.assert(solution.numWaysMemo(words2, target2) === 4, "Test case 2 memo failed");
    console.assert(solution.numWaysES6(words2, target2) === 4, "Test case 2 ES6 failed");
    
    // Edge cases
    const words3 = ["a", "b"];
    const target3 = "ab";
    console.assert(solution.numWays(words3, target3) === 1, "Edge case failed");
    
    const words4 = ["abc"];
    const target4 = "abcd";
    console.assert(solution.numWays(words4, target4) === 0, "Edge case 2 failed");
    
    console.log("All JavaScript test cases passed!");
}

// Function to demonstrate the solution with detailed output
function demonstrateSolution(words, target) {
    const solution = new Solution();
    
    console.log(`\n=== JavaScript Analysis: words = [${words.map(w => `"${w}"`).join(', ')}], target = "${target}" ===`);
    
    // Show character frequency analysis
    const n = words[0].length;
    const freq = Array(n).fill().map(() => Array(26).fill(0));
    for (const word of words) {
        for (let i = 0; i < n; i++) {
            freq[i][word.charCodeAt(i) - 97]++;
        }
    }
    
    console.log("Character frequency at each position:");
    for (let i = 0; i < n; i++) {
        let output = `Position ${i}: `;
        for (let j = 0; j < 26; j++) {
            if (freq[i][j] > 0) {
                output += `${String.fromCharCode(97 + j)}=${freq[i][j]} `;
            }
        }
        console.log(output);
    }
    
    const result = solution.numWays(words, target);
    console.log(`Number of ways: ${result}`);
}

// Performance comparison
function performanceComparison() {
    const solution = new Solution();
    const words = ["acca", "bbbb", "caca"];
    const target = "aba";
    
    const approaches = [
        ["2D DP", solution.numWays.bind(solution)],
        ["Optimized", solution.numWaysOptimized.bind(solution)],
        ["Memoized", solution.numWaysMemo.bind(solution)],
        ["ES6 Map", solution.numWaysES6.bind(solution)]
    ];
    
    console.log("\n=== Performance Comparison ===");
    for (const [name, method] of approaches) {
        const start = performance.now();
        const result = method(words, target);
        const end = performance.now();
        console.log(`${name}: ${result} (Time: ${(end - start).toFixed(4)}ms)`);
    }
}

// Main function
function main() {
    console.log("LeetCode 1639: Target String Formation - JavaScript Solution");
    console.log("============================================================");
    
    // Run tests
    runTests();
    
    // Demonstrate examples
    const words1 = ["acca", "bbbb", "caca"];
    const target1 = "aba";
    demonstrateSolution(words1, target1);
    
    const words2 = ["abba", "baab"];
    const target2 = "bab";
    demonstrateSolution(words2, target2);
    
    // Performance comparison
    performanceComparison();
    
    // Interactive mode for Node.js
    if (typeof require !== 'undefined') {
        console.log("\n=== Interactive Mode ===");
        const readline = require('readline');
        const rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });
        
        rl.question('Enter words (comma-separated): ', (wordsInput) => {
            rl.question('Enter target string: ', (target) => {
                const words = wordsInput.split(',').map(w => w.trim());
                
                if (words.length === 0 || target.length === 0) {
                    console.log("Invalid input!");
                } else {
                    const solution = new Solution();
                    const result = solution.numWays(words, target);
                    console.log(`Number of ways: ${result}`);
                }
                
                rl.close();
            });
        });
    }
}

// Export for Node.js or run in browser
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { Solution, runTests, demonstrateSolution };
} else {
    // Run main function if in browser or direct execution
    main();
}

// For LeetCode submission - clean version
/*
var numWays = function(words, target) {
    const MOD = 1000000007;
    const m = target.length;
    const n = words[0].length;
    
    if (m > n) return 0;
    
    const freq = Array(n).fill().map(() => Array(26).fill(0));
    for (const word of words) {
        for (let i = 0; i < n; i++) {
            freq[i][word.charCodeAt(i) - 97]++;
        }
    }
    
    const dp = Array(m + 1).fill().map(() => Array(n + 1).fill(0));
    
    for (let j = 0; j <= n; j++) {
        dp[0][j] = 1;
    }
    
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            dp[i][j] = dp[i][j-1];
            
            const charIndex = target.charCodeAt(i-1) - 97;
            if (freq[j-1][charIndex] > 0) {
                dp[i][j] = (dp[i][j] + (dp[i-1][j-1] * freq[j-1][charIndex]) % MOD) % MOD;
            }
        }
    }
    
    return dp[m][n];
};
*/
