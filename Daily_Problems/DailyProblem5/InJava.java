package Daily_Problems.DailyProblem5;

import java.util.*;

class Solution {
    // Approach 1: Brute Force - O(n) time, O(1) space
    public int differenceOfSumsBruteForce(int n, int m) {
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
    public int differenceOfSums(int n, int m) {
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
    
    // Alternative mathematical approach - most concise
    public int differenceOfSumsAlternative(int n, int m) {
        // Total sum from 1 to n
        int totalSum = n * (n + 1) / 2;
        
        // Sum of multiples of m
        int multiplesCount = n / m;
        int sumOfMultiples = m * multiplesCount * (multiplesCount + 1) / 2;
        
        // num1 - num2 = (totalSum - sumOfMultiples) - sumOfMultiples
        // = totalSum - 2 * sumOfMultiples
        return totalSum - 2 * sumOfMultiples;
    }
}

public class InJava {
    // Test function
    public static void runTests() {
        Solution solution = new Solution();
        
        // Test case 1
        assert solution.differenceOfSums(10, 3) == 19;
        assert solution.differenceOfSumsBruteForce(10, 3) == 19;
        assert solution.differenceOfSumsAlternative(10, 3) == 19;
        
        // Test case 2
        assert solution.differenceOfSums(5, 6) == 15;
        assert solution.differenceOfSumsBruteForce(5, 6) == 15;
        assert solution.differenceOfSumsAlternative(5, 6) == 15;
        
        // Test case 3
        assert solution.differenceOfSums(5, 1) == -15;
        assert solution.differenceOfSumsBruteForce(5, 1) == -15;
        assert solution.differenceOfSumsAlternative(5, 1) == -15;
        
        // Additional test cases
        assert solution.differenceOfSums(1, 2) == 1;
        assert solution.differenceOfSums(4, 2) == -2;
        assert solution.differenceOfSums(1000, 7) == 84735;
        
        System.out.println("All test cases passed!");
    }
    
    // Function to demonstrate the solution with detailed output
    public static void demonstrateSolution(int n, int m) {
        Solution solution = new Solution();
        
        System.out.println("\n=== Solving for n = " + n + ", m = " + m + " ===");
        
        // Show brute force approach
        int num1 = 0, num2 = 0;
        List<Integer> nonDivisible = new ArrayList<>();
        List<Integer> divisible = new ArrayList<>();
        
        for (int i = 1; i <= n; i++) {
            if (i % m == 0) {
                num2 += i;
                divisible.add(i);
            } else {
                num1 += i;
                nonDivisible.add(i);
            }
        }
        
        System.out.print("Numbers not divisible by " + m + ": ");
        for (int i = 0; i < nonDivisible.size(); i++) {
            System.out.print(nonDivisible.get(i));
            if (i < nonDivisible.size() - 1) System.out.print(", ");
        }
        System.out.println(" -> sum = " + num1);
        
        System.out.print("Numbers divisible by " + m + ": ");
        for (int i = 0; i < divisible.size(); i++) {
            System.out.print(divisible.get(i));
            if (i < divisible.size() - 1) System.out.print(", ");
        }
        System.out.println(" -> sum = " + num2);
        
        int result = solution.differenceOfSums(n, m);
        System.out.println("Result: " + num1 + " - " + num2 + " = " + result);
    }
    
    public static void main(String[] args) {
        System.out.println("LeetCode 2894: Divisible and Non-divisible Sums Difference");
        System.out.println("=========================================================");
        
        // Run all test cases
        runTests();
        
        // Demonstrate with examples
        demonstrateSolution(10, 3);
        demonstrateSolution(5, 6);
        demonstrateSolution(5, 1);
        
        // Interactive input
        System.out.println("\n=== Interactive Mode ===");
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter n: ");
        int n = scanner.nextInt();
        System.out.print("Enter m: ");
        int m = scanner.nextInt();
        
        Solution solution = new Solution();
        int result = solution.differenceOfSums(n, m);
        System.out.println("Result for n=" + n + ", m=" + m + ": " + result);
        
        scanner.close();
    }
}