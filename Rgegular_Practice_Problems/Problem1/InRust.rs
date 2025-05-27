// LeetCode 1639: Number of Ways to Form a Target String Given a Dictionary
// Rust Solution with Multiple Approaches

use std::collections::HashMap;

impl Solution {
    /// Approach 1: 2D Dynamic Programming with Character Frequency Preprocessing
    /// Time: O(m * n * k), Space: O(m * n + k * 26)
    pub fn num_ways_to_form_target_2d_dp(words: Vec<String>, target: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let m = target.len();
        let n = words[0].len();
        let target_chars: Vec<char> = target.chars().collect();
        
        // Precompute character frequencies at each position
        let mut freq = vec![vec![0i64; 26]; n];
        for word in &words {
            for (j, ch) in word.chars().enumerate() {
                freq[j][(ch as u8 - b'a') as usize] += 1;
            }
        }
        
        // dp[i][j] = ways to form target[0..i] using words[0..j]
        let mut dp = vec![vec![0i64; n + 1]; m + 1];
        
        // Base case: empty target can be formed in 1 way
        for j in 0..=n {
            dp[0][j] = 1;
        }
        
        for i in 1..=m {
            for j in 1..=n {
                // Don't use current position
                dp[i][j] = dp[i][j - 1];
                
                // Use current position if character matches
                let char_idx = (target_chars[i - 1] as u8 - b'a') as usize;
                if freq[j - 1][char_idx] > 0 {
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1] * freq[j - 1][char_idx]) % MOD;
                }
            }
        }
        
        dp[m][n] as i32
    }
    
    /// Approach 2: Space-Optimized 1D DP
    /// Time: O(m * n * k), Space: O(m + k * 26)
    pub fn num_ways_to_form_target_optimized(words: Vec<String>, target: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let m = target.len();
        let n = words[0].len();
        let target_chars: Vec<char> = target.chars().collect();
        
        // Precompute character frequencies
        let mut freq = vec![vec![0i64; 26]; n];
        for word in &words {
            for (j, ch) in word.chars().enumerate() {
                freq[j][(ch as u8 - b'a') as usize] += 1;
            }
        }
        
        // Use 1D DP array
        let mut dp = vec![0i64; m + 1];
        dp[0] = 1; // Base case
        
        for j in 0..n {
            // Process from right to left to avoid overwriting
            for i in (1..=m).rev() {
                let char_idx = (target_chars[i - 1] as u8 - b'a') as usize;
                if freq[j][char_idx] > 0 {
                    dp[i] = (dp[i] + dp[i - 1] * freq[j][char_idx]) % MOD;
                }
            }
        }
        
        dp[m] as i32
    }
    
    /// Approach 3: Memoized Recursion with Character Frequency Map
    /// Time: O(m * n * k), Space: O(m * n + k * 26)
    pub fn num_ways_to_form_target_memo(words: Vec<String>, target: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = words[0].len();
        let target_chars: Vec<char> = target.chars().collect();
        
        // Precompute frequencies
        let mut freq = vec![vec![0i64; 26]; n];
        for word in &words {
            for (j, ch) in word.chars().enumerate() {
                freq[j][(ch as u8 - b'a') as usize] += 1;
            }
        }
        
        let mut memo = HashMap::new();
        
        fn dfs(
            target_idx: usize,
            word_idx: usize,
            target_chars: &[char],
            freq: &[Vec<i64>],
            memo: &mut HashMap<(usize, usize), i64>,
        ) -> i64 {
            const MOD: i64 = 1_000_000_007;
            
            // Base cases
            if target_idx == target_chars.len() {
                return 1;
            }
            if word_idx == freq.len() {
                return 0;
            }
            
            if let Some(&cached) = memo.get(&(target_idx, word_idx)) {
                return cached;
            }
            
            // Skip current position
            let mut result = dfs(target_idx, word_idx + 1, target_chars, freq, memo);
            
            // Use current position if character matches
            let char_idx = (target_chars[target_idx] as u8 - b'a') as usize;
            if freq[word_idx][char_idx] > 0 {
                let ways_with_current = dfs(target_idx + 1, word_idx + 1, target_chars, freq, memo);
                result = (result + ways_with_current * freq[word_idx][char_idx]) % MOD;
            }
            
            memo.insert((target_idx, word_idx), result);
            result
        }
        
        dfs(0, 0, &target_chars, &freq, &mut memo) as i32
    }
    
    /// Approach 4: Bottom-Up DP with Early Termination Optimization
    /// Time: O(m * n * k), Space: O(m + k * 26)
    pub fn num_ways_to_form_target_optimized_v2(words: Vec<String>, target: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let m = target.len();
        let n = words[0].len();
        
        // Early termination: impossible if target longer than word length
        if m > n {
            return 0;
        }
        
        let target_chars: Vec<char> = target.chars().collect();
        
        // Precompute frequencies with early exit optimization
        let mut freq = vec![vec![0i64; 26]; n];
        for word in &words {
            for (j, ch) in word.chars().enumerate() {
                freq[j][(ch as u8 - b'a') as usize] += 1;
            }
        }
        
        // Check if all target characters exist in dictionary
        let mut target_char_exists = vec![false; 26];
        for ch in &target_chars {
            target_char_exists[(*ch as u8 - b'a') as usize] = true;
        }
        
        for i in 0..26 {
            if target_char_exists[i] {
                let mut found = false;
                for j in 0..n {
                    if freq[j][i] > 0 {
                        found = true;
                        break;
                    }
                }
                if !found {
                    return 0; // Target character not found in any word
                }
            }
        }
        
        let mut dp = vec![0i64; m + 1];
        dp[0] = 1;
        
        for j in 0..n {
            for i in (1..=m.min(j + 1)).rev() {
                let char_idx = (target_chars[i - 1] as u8 - b'a') as usize;
                if freq[j][char_idx] > 0 {
                    dp[i] = (dp[i] + dp[i - 1] * freq[j][char_idx]) % MOD;
                }
            }
        }
        
        dp[m] as i32
    }
}

// Test structure for Rust
struct Solution;

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_basic_cases() {
        let words1 = vec!["acca".to_string(), "bbbb".to_string(), "caca".to_string()];
        let target1 = "aba".to_string();
        assert_eq!(Solution::num_ways_to_form_target_2d_dp(words1.clone(), target1.clone()), 6);
        assert_eq!(Solution::num_ways_to_form_target_optimized(words1.clone(), target1.clone()), 6);
        assert_eq!(Solution::num_ways_to_form_target_memo(words1.clone(), target1.clone()), 6);
        assert_eq!(Solution::num_ways_to_form_target_optimized_v2(words1, target1), 6);
        
        let words2 = vec!["abcd".to_string()];
        let target2 = "abcd".to_string();
        assert_eq!(Solution::num_ways_to_form_target_2d_dp(words2.clone(), target2.clone()), 1);
        assert_eq!(Solution::num_ways_to_form_target_optimized(words2.clone(), target2.clone()), 1);
        assert_eq!(Solution::num_ways_to_form_target_memo(words2.clone(), target2.clone()), 1);
        assert_eq!(Solution::num_ways_to_form_target_optimized_v2(words2, target2), 1);
    }
    
    #[test]
    fn test_edge_cases() {
        let words = vec!["abcd".to_string()];
        let target = "abcde".to_string();
        assert_eq!(Solution::num_ways_to_form_target_2d_dp(words.clone(), target.clone()), 0);
        assert_eq!(Solution::num_ways_to_form_target_optimized(words.clone(), target.clone()), 0);
        assert_eq!(Solution::num_ways_to_form_target_memo(words.clone(), target.clone()), 0);
        assert_eq!(Solution::num_ways_to_form_target_optimized_v2(words, target), 0);
    }
    
    #[test]
    fn test_performance() {
        // Test with larger input
        let words: Vec<String> = (0..1000).map(|i| format!("abc{}", i % 10)).collect();
        let target = "abc".to_string();
        
        let start = std::time::Instant::now();
        let result = Solution::num_ways_to_form_target_optimized(words, target);
        let duration = start.elapsed();
        
        println!("Rust optimized solution took: {:?}", duration);
        println!("Result: {}", result);
    }
}

fn main() {
    // Interactive testing
    let words = vec!["acca".to_string(), "bbbb".to_string(), "caca".to_string()];
    let target = "aba".to_string();
    
    println!("=== LeetCode 1639: Number of Ways to Form Target String ===");
    println!("Words: {:?}", words);
    println!("Target: {}", target);
    println!();
    
    let start = std::time::Instant::now();
    let result1 = Solution::num_ways_to_form_target_2d_dp(words.clone(), target.clone());
    let time1 = start.elapsed();
    
    let start = std::time::Instant::now();
    let result2 = Solution::num_ways_to_form_target_optimized(words.clone(), target.clone());
    let time2 = start.elapsed();
    
    let start = std::time::Instant::now();
    let result3 = Solution::num_ways_to_form_target_memo(words.clone(), target.clone());
    let time3 = start.elapsed();
    
    let start = std::time::Instant::now();
    let result4 = Solution::num_ways_to_form_target_optimized_v2(words, target);
    let time4 = start.elapsed();
    
    println!("Results:");
    println!("2D DP: {} (Time: {:?})", result1, time1);
    println!("Space-Optimized: {} (Time: {:?})", result2, time2);
    println!("Memoized Recursion: {} (Time: {:?})", result3, time3);
    println!("Optimized v2: {} (Time: {:?})", result4, time4);
}
