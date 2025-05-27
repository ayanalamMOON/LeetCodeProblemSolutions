use std::io;

struct Solution;

impl Solution {
    /// Brute Force Approach - O(n) time, O(1) space
    pub fn difference_of_sums_brute_force(n: i32, m: i32) -> i32 {
        let mut num1 = 0; // sum of numbers not divisible by m
        let mut num2 = 0; // sum of numbers divisible by m
        
        for i in 1..=n {
            if i % m == 0 {
                num2 += i;
            } else {
                num1 += i;
            }
        }
        
        num1 - num2
    }
    
    /// Mathematical Formula Approach - O(1) time, O(1) space
    pub fn difference_of_sums(n: i32, m: i32) -> i32 {
        // Total sum of numbers from 1 to n
        let total_sum = n * (n + 1) / 2;
        
        // Number of multiples of m in range [1, n]
        let multiples_count = n / m;
        
        // Sum of multiples of m: m + 2m + 3m + ... + (multiples_count * m)
        // = m * (1 + 2 + 3 + ... + multiples_count)
        // = m * (multiples_count * (multiples_count + 1) / 2)
        let num2 = m * multiples_count * (multiples_count + 1) / 2;
        
        // Sum of non-multiples = total_sum - sum of multiples
        let num1 = total_sum - num2;
        
        num1 - num2
    }
    
    /// Alternative Mathematical Approach - most concise
    pub fn difference_of_sums_alternative(n: i32, m: i32) -> i32 {
        let total_sum = n * (n + 1) / 2;
        let multiples_count = n / m;
        let sum_of_multiples = m * multiples_count * (multiples_count + 1) / 2;
        
        // num1 - num2 = (total_sum - sum_of_multiples) - sum_of_multiples
        // = total_sum - 2 * sum_of_multiples
        total_sum - 2 * sum_of_multiples
    }
}

/// Test function to verify all approaches work correctly
fn run_tests() {
    // Test case 1
    assert_eq!(Solution::difference_of_sums(10, 3), 19);
    assert_eq!(Solution::difference_of_sums_brute_force(10, 3), 19);
    assert_eq!(Solution::difference_of_sums_alternative(10, 3), 19);
    
    // Test case 2
    assert_eq!(Solution::difference_of_sums(5, 6), 15);
    assert_eq!(Solution::difference_of_sums_brute_force(5, 6), 15);
    assert_eq!(Solution::difference_of_sums_alternative(5, 6), 15);
    
    // Test case 3
    assert_eq!(Solution::difference_of_sums(5, 1), -15);
    assert_eq!(Solution::difference_of_sums_brute_force(5, 1), -15);
    assert_eq!(Solution::difference_of_sums_alternative(5, 1), -15);
    
    // Additional test cases
    assert_eq!(Solution::difference_of_sums(1, 2), 1);
    assert_eq!(Solution::difference_of_sums(4, 2), -2);
    assert_eq!(Solution::difference_of_sums(1000, 7), 84735);
    
    println!("All test cases passed!");
}

/// Function to demonstrate the solution with detailed output
fn demonstrate_solution(n: i32, m: i32) {
    println!("\n=== Solving for n = {}, m = {} ===", n, m);
    
    // Show brute force approach
    let mut num1 = 0;
    let mut num2 = 0;
    let mut non_divisible = Vec::new();
    let mut divisible = Vec::new();
    
    for i in 1..=n {
        if i % m == 0 {
            num2 += i;
            divisible.push(i);
        } else {
            num1 += i;
            non_divisible.push(i);
        }
    }
    
    println!("Numbers not divisible by {}: {:?} -> sum = {}", m, non_divisible, num1);
    println!("Numbers divisible by {}: {:?} -> sum = {}", m, divisible, num2);
    
    let result = Solution::difference_of_sums(n, m);
    println!("Result: {} - {} = {}", num1, num2, result);
}

/// Function to get user input with error handling
fn get_input(prompt: &str) -> Result<i32, Box<dyn std::error::Error>> {
    println!("{}", prompt);
    let mut input = String::new();
    io::stdin().read_line(&mut input)?;
    let number: i32 = input.trim().parse()?;
    Ok(number)
}

/// Performance comparison function
fn performance_comparison() {
    println!("\n=== Performance Comparison ===");
    let n = 1000;
    let m = 7;
    
    use std::time::Instant;
    
    // Measure brute force approach
    let start = Instant::now();
    let result_brute = Solution::difference_of_sums_brute_force(n, m);
    let duration_brute = start.elapsed();
    
    // Measure mathematical approach
    let start = Instant::now();
    let result_math = Solution::difference_of_sums(n, m);
    let duration_math = start.elapsed();
    
    println!("Brute Force: {} (Time: {:?})", result_brute, duration_brute);
    println!("Mathematical: {} (Time: {:?})", result_math, duration_math);
    println!("Results match: {}", result_brute == result_math);
}

/// Main function
fn main() {
    println!("LeetCode 2894: Divisible and Non-divisible Sums Difference");
    println!("=========================================================");
    
    // Run all test cases
    run_tests();
    
    // Demonstrate with examples
    demonstrate_solution(10, 3);
    demonstrate_solution(5, 6);
    demonstrate_solution(5, 1);
    
    // Performance comparison
    performance_comparison();
    
    // Interactive input
    println!("\n=== Interactive Mode ===");
    match get_input("Enter n:") {
        Ok(n) => {
            match get_input("Enter m:") {
                Ok(m) => {
                    if n > 0 && m > 0 {
                        let result = Solution::difference_of_sums(n, m);
                        println!("Result for n={}, m={}: {}", n, m, result);
                    } else {
                        println!("Please enter positive integers!");
                    }
                }
                Err(e) => println!("Error reading m: {}", e),
            }
        }
        Err(e) => println!("Error reading n: {}", e),
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_example_cases() {
        assert_eq!(Solution::difference_of_sums(10, 3), 19);
        assert_eq!(Solution::difference_of_sums(5, 6), 15);
        assert_eq!(Solution::difference_of_sums(5, 1), -15);
    }
    
    #[test]
    fn test_edge_cases() {
        assert_eq!(Solution::difference_of_sums(1, 2), 1);
        assert_eq!(Solution::difference_of_sums(4, 2), -2);
        assert_eq!(Solution::difference_of_sums(1, 1), -1);
    }
    
    #[test]
    fn test_approaches_consistency() {
        let test_cases = vec![(10, 3), (5, 6), (5, 1), (100, 7), (50, 13)];
        
        for (n, m) in test_cases {
            let brute_result = Solution::difference_of_sums_brute_force(n, m);
            let math_result = Solution::difference_of_sums(n, m);
            let alt_result = Solution::difference_of_sums_alternative(n, m);
            
            assert_eq!(brute_result, math_result, "Brute force and math differ for n={}, m={}", n, m);
            assert_eq!(math_result, alt_result, "Math and alternative differ for n={}, m={}", n, m);
        }
    }
    
    #[test]
    fn test_large_numbers() {
        assert_eq!(Solution::difference_of_sums(1000, 7), 84735);
        assert_eq!(Solution::difference_of_sums(999, 13), 38350);
    }
}

/* 
LeetCode submission format:

impl Solution {
    pub fn difference_of_sums(n: i32, m: i32) -> i32 {
        let total_sum = n * (n + 1) / 2;
        let multiples_count = n / m;
        let sum_of_multiples = m * multiples_count * (multiples_count + 1) / 2;
        total_sum - 2 * sum_of_multiples
    }
}
*/
