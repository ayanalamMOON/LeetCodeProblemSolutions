/**
 * @param {number} n
 * @param {number} m
 * @return {number}
 */

class Solution {
    // Brute Force Approach - O(n) time, O(1) space
    differenceOfSumsBruteForce(n, m) {
        let num1 = 0; // sum of numbers not divisible by m
        let num2 = 0; // sum of numbers divisible by m
        
        for (let i = 1; i <= n; i++) {
            if (i % m === 0) {
                num2 += i;
            } else {
                num1 += i;
            }
        }
        
        return num1 - num2;
    }
    
    // Mathematical Formula Approach - O(1) time, O(1) space
    differenceOfSums(n, m) {
        // Total sum of numbers from 1 to n
        const totalSum = n * (n + 1) / 2;
        
        // Number of multiples of m in range [1, n]
        const multiplesCount = Math.floor(n / m);
        
        // Sum of multiples of m: m + 2m + 3m + ... + (multiplesCount * m)
        // = m * (1 + 2 + 3 + ... + multiplesCount)
        // = m * (multiplesCount * (multiplesCount + 1) / 2)
        const num2 = m * multiplesCount * (multiplesCount + 1) / 2;
        
        // Sum of non-multiples = totalSum - sum of multiples
        const num1 = totalSum - num2;
        
        return num1 - num2;
    }
    
    // Alternative Mathematical Approach - most concise
    differenceOfSumsAlternative(n, m) {
        const totalSum = n * (n + 1) / 2;
        const multiplesCount = Math.floor(n / m);
        const sumOfMultiples = m * multiplesCount * (multiplesCount + 1) / 2;
        
        // num1 - num2 = (totalSum - sumOfMultiples) - sumOfMultiples
        // = totalSum - 2 * sumOfMultiples
        return totalSum - 2 * sumOfMultiples;
    }
}

// Test function
function runTests() {
    const solution = new Solution();
    
    // Test case 1
    console.assert(solution.differenceOfSums(10, 3) === 19, "Test case 1 failed");
    console.assert(solution.differenceOfSumsBruteForce(10, 3) === 19, "Test case 1 brute force failed");
    console.assert(solution.differenceOfSumsAlternative(10, 3) === 19, "Test case 1 alternative failed");
    
    // Test case 2
    console.assert(solution.differenceOfSums(5, 6) === 15, "Test case 2 failed");
    console.assert(solution.differenceOfSumsBruteForce(5, 6) === 15, "Test case 2 brute force failed");
    console.assert(solution.differenceOfSumsAlternative(5, 6) === 15, "Test case 2 alternative failed");
    
    // Test case 3
    console.assert(solution.differenceOfSums(5, 1) === -15, "Test case 3 failed");
    console.assert(solution.differenceOfSumsBruteForce(5, 1) === -15, "Test case 3 brute force failed");
    console.assert(solution.differenceOfSumsAlternative(5, 1) === -15, "Test case 3 alternative failed");
    
    // Additional test cases
    console.assert(solution.differenceOfSums(1, 2) === 1, "Additional test case 1 failed");
    console.assert(solution.differenceOfSums(4, 2) === -2, "Additional test case 2 failed");
    console.assert(solution.differenceOfSums(1000, 7) === 84735, "Additional test case 3 failed");
    
    console.log("All test cases passed!");
}

// Function to demonstrate the solution with detailed output
function demonstrateSolution(n, m) {
    const solution = new Solution();
    
    console.log(`\n=== Solving for n = ${n}, m = ${m} ===`);
    
    // Show brute force approach
    let num1 = 0;
    let num2 = 0;
    const nonDivisible = [];
    const divisible = [];
    
    for (let i = 1; i <= n; i++) {
        if (i % m === 0) {
            num2 += i;
            divisible.push(i);
        } else {
            num1 += i;
            nonDivisible.push(i);
        }
    }
    
    console.log(`Numbers not divisible by ${m}: [${nonDivisible.join(', ')}] -> sum = ${num1}`);
    console.log(`Numbers divisible by ${m}: [${divisible.join(', ')}] -> sum = ${num2}`);
    
    const result = solution.differenceOfSums(n, m);
    console.log(`Result: ${num1} - ${num2} = ${result}`);
}

// Main function
function main() {
    console.log("LeetCode 2894: Divisible and Non-divisible Sums Difference");
    console.log("=========================================================");
    
    // Run all test cases
    runTests();
    
    // Demonstrate with examples
    demonstrateSolution(10, 3);
    demonstrateSolution(5, 6);
    demonstrateSolution(5, 1);
    
    // For Node.js environment - interactive input
    if (typeof require !== 'undefined') {
        console.log("\n=== Interactive Mode ===");
        const readline = require('readline');
        const rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });
        
        rl.question('Enter n: ', (nInput) => {
            rl.question('Enter m: ', (mInput) => {
                const n = parseInt(nInput);
                const m = parseInt(mInput);
                
                if (isNaN(n) || isNaN(m)) {
                    console.log("Please enter valid integers!");
                } else {
                    const solution = new Solution();
                    const result = solution.differenceOfSums(n, m);
                    console.log(`Result for n=${n}, m=${m}: ${result}`);
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
var differenceOfSums = function(n, m) {
    const totalSum = n * (n + 1) / 2;
    const multiplesCount = Math.floor(n / m);
    const sumOfMultiples = m * multiplesCount * (multiplesCount + 1) / 2;
    return totalSum - 2 * sumOfMultiples;
};
*/
