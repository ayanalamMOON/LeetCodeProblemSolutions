#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

class Solution {
public:
    // Approach 1: Brute Force - O(n) time, O(1) space
    int differenceOfSums_BruteForce(int n, int m) {
        int num1 = 0; // sum of numbers not divisible by m
        int num2 = 0; // sum of numbers divisible by m
        
        for (int i = 1; i <= n; i++) {
            if (i % m == 0) {
                num2 += i;
            } else {
                num1 += i;
            }
        }
        
        return num1 - num2;
    }
    
    // Approach 2: Mathematical Formula - O(1) time, O(1) space
    int differenceOfSums(int n, int m) {
        // Total sum of numbers from 1 to n
        int totalSum = n * (n + 1) / 2;
        
        // Number of multiples of m in range [1, n]
        int multiplesCount = n / m;
        
        // Sum of multiples of m: m + 2m + 3m + ... + (multiplesCount * m)
        // = m * (1 + 2 + 3 + ... + multiplesCount)
        // = m * (multiplesCount * (multiplesCount + 1) / 2)
        int num2 = m * multiplesCount * (multiplesCount + 1) / 2;
        
        // Sum of non-multiples = totalSum - sum of multiples
        int num1 = totalSum - num2;
        
        return num1 - num2;
    }
    
    // Alternative mathematical approach
    int differenceOfSums_Alternative(int n, int m) {
        // Total sum from 1 to n
        int totalSum = n * (n + 1) / 2;
        
        // Sum of multiples of m
        int multiplesCount = n / m;
        int sumOfMultiples = m * multiplesCount * (multiplesCount + 1) / 2;
        
        // num1 - num2 = (totalSum - sumOfMultiples) - sumOfMultiples
        // = totalSum - 2 * sumOfMultiples
        return totalSum - 2 * sumOfMultiples;
    }
};

// Test function
void runTests() {
    Solution solution;
    
    // Test case 1
    assert(solution.differenceOfSums(10, 3) == 19);
    assert(solution.differenceOfSums_BruteForce(10, 3) == 19);
    assert(solution.differenceOfSums_Alternative(10, 3) == 19);
    
    // Test case 2
    assert(solution.differenceOfSums(5, 6) == 15);
    assert(solution.differenceOfSums_BruteForce(5, 6) == 15);
    assert(solution.differenceOfSums_Alternative(5, 6) == 15);
    
    // Test case 3
    assert(solution.differenceOfSums(5, 1) == -15);
    assert(solution.differenceOfSums_BruteForce(5, 1) == -15);
    assert(solution.differenceOfSums_Alternative(5, 1) == -15);
    
    // Additional test cases
    assert(solution.differenceOfSums(1, 2) == 1);
    assert(solution.differenceOfSums(4, 2) == -2);
    assert(solution.differenceOfSums(1000, 7) == 84735);
    
    cout << "All test cases passed!" << endl;
}

// Function to demonstrate the solution with detailed output
void demonstrateSolution(int n, int m) {
    Solution solution;
    
    cout << "\n=== Solving for n = " << n << ", m = " << m << " ===" << endl;
    
    // Show brute force approach
    int num1 = 0, num2 = 0;
    vector<int> nonDivisible, divisible;
    
    for (int i = 1; i <= n; i++) {
        if (i % m == 0) {
            num2 += i;
            divisible.push_back(i);
        } else {
            num1 += i;
            nonDivisible.push_back(i);
        }
    }
    
    cout << "Numbers not divisible by " << m << ": ";
    for (int i = 0; i < nonDivisible.size(); i++) {
        cout << nonDivisible[i];
        if (i < nonDivisible.size() - 1) cout << ", ";
    }
    cout << " -> sum = " << num1 << endl;
    
    cout << "Numbers divisible by " << m << ": ";
    for (int i = 0; i < divisible.size(); i++) {
        cout << divisible[i];
        if (i < divisible.size() - 1) cout << ", ";
    }
    cout << " -> sum = " << num2 << endl;
    
    int result = solution.differenceOfSums(n, m);
    cout << "Result: " << num1 << " - " << num2 << " = " << result << endl;
}

int main() {
    cout << "LeetCode 2894: Divisible and Non-divisible Sums Difference" << endl;
    cout << "=========================================================" << endl;
    
    // Run all test cases
    runTests();
    
    // Demonstrate with examples
    demonstrateSolution(10, 3);
    demonstrateSolution(5, 6);
    demonstrateSolution(5, 1);
    
    // Interactive input
    cout << "\n=== Interactive Mode ===" << endl;
    int n, m;
    cout << "Enter n: ";
    cin >> n;
    cout << "Enter m: ";
    cin >> m;
    
    Solution solution;
    int result = solution.differenceOfSums(n, m);
    cout << "Result for n=" << n << ", m=" << m << ": " << result << endl;
    
    return 0;
}