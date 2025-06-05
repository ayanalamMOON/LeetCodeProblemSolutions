/**
 * @file InRust.rs
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

struct UnionFind {
    parent: Vec<usize>,
}

impl UnionFind {
    /// Create new Union Find structure for 26 characters
    fn new() -> Self {
        UnionFind {
            parent: (0..26).collect(),
        }
    }

    /// Find operation with path compression
    ///
    /// # Arguments
    /// * `x` - Character index (0-25 for 'a'-'z')
    ///
    /// # Returns
    /// Root representative of x's equivalence class
    fn find(&mut self, x: usize) -> usize {
        if self.parent[x] != x {
            self.parent[x] = self.find(self.parent[x]); // Path compression
        }
        self.parent[x]
    }

    /// Union operation with lexicographical preference
    ///
    /// # Arguments
    /// * `x` - First character index
    /// * `y` - Second character index
    fn unite(&mut self, x: usize, y: usize) {
        let root_x = self.find(x);
        let root_y = self.find(y);
        if root_x != root_y {
            // Always make smaller character the root for lexicographical order
            if root_x < root_y {
                self.parent[root_y] = root_x;
            } else {
                self.parent[root_x] = root_y;
            }
        }
    }
}

impl Solution {
    /// Find lexicographically smallest equivalent string
    ///
    /// # Arguments
    /// * `s1` - First equivalence string
    /// * `s2` - Second equivalence string
    /// * `base_str` - Base string to transform
    ///
    /// # Returns
    /// Lexicographically smallest equivalent string
    pub fn smallest_equivalent_string(s1: String, s2: String, base_str: String) -> String {
        let mut uf = UnionFind::new();

        // Build equivalence relationships
        let s1_chars: Vec<char> = s1.chars().collect();
        let s2_chars: Vec<char> = s2.chars().collect();

        for i in 0..s1_chars.len() {
            let x = (s1_chars[i] as usize) - ('a' as usize);
            let y = (s2_chars[i] as usize) - ('a' as usize);
            uf.unite(x, y);
        }

        // Transform baseStr using equivalence mappings
        base_str
            .chars()
            .map(|c| {
                let idx = (c as usize) - ('a' as usize);
                let root = uf.find(idx);
                char::from(('a' as u8) + (root as u8))
            })
            .collect()
    }
}

/// Alternative implementation with standalone functions
mod standalone {
    /// Find operation with path compression (standalone version)
    fn find(parent: &mut Vec<usize>, x: usize) -> usize {
        if parent[x] != x {
            parent[x] = find(parent, parent[x]);
        }
        parent[x]
    }

    /// Union operation with lexicographical preference (standalone version)
    fn unite(parent: &mut Vec<usize>, x: usize, y: usize) {
        let root_x = find(parent, x);
        let root_y = find(parent, y);
        if root_x != root_y {
            if root_x < root_y {
                parent[root_y] = root_x;
            } else {
                parent[root_x] = root_y;
            }
        }
    }

    /// Alternative implementation using standalone functions
    pub fn smallest_equivalent_string_alt(s1: String, s2: String, base_str: String) -> String {
        let mut parent: Vec<usize> = (0..26).collect();

        // Build equivalence relationships
        let s1_bytes = s1.as_bytes();
        let s2_bytes = s2.as_bytes();

        for i in 0..s1_bytes.len() {
            let x = (s1_bytes[i] - b'a') as usize;
            let y = (s2_bytes[i] - b'a') as usize;
            unite(&mut parent, x, y);
        }

        // Transform baseStr
        base_str
            .bytes()
            .map(|b| {
                let idx = (b - b'a') as usize;
                let root = find(&mut parent, idx);
                (b'a' + root as u8) as char
            })
            .collect()
    }
}

/// Benchmark struct for performance testing
#[derive(Debug)]
struct TestCase {
    s1: &'static str,
    s2: &'static str,
    base_str: &'static str,
    expected: &'static str,
}

impl TestCase {
    fn new(s1: &'static str, s2: &'static str, base_str: &'static str, expected: &'static str) -> Self {
        TestCase { s1, s2, base_str, expected }
    }
}

/// Test driver function
fn main() {
    println!("Testing LeetCode 1061: Lexicographically Smallest Equivalent String");

    let test_cases = vec![
        TestCase::new("parker", "morris", "parser", "makkek"),
        TestCase::new("hello", "world", "hold", "hdld"),
        TestCase::new("leetcode", "programs", "sourcecode", "aauaaaaada"),
        TestCase::new("aa", "aa", "abc", "abc"), // No equivalences
        TestCase::new("abc", "aaa", "xyz", "aaa"), // All map to 'a'
        TestCase::new("a", "b", "c", "a"), // Single character
        TestCase::new("ab", "cd", "", ""), // Empty base string
        TestCase::new("abcdefg", "bcdefgh", "ghijklm", "aaaaaaa"), // Long chain
    ];

    println!("\n=== Testing struct-based implementation ===");
    for (i, test) in test_cases.iter().enumerate() {
        let result = Solution::smallest_equivalent_string(
            test.s1.to_string(),
            test.s2.to_string(),
            test.base_str.to_string(),
        );

        let status = if result == test.expected { "✓ PASS" } else { "✗ FAIL" };
        println!("Test {}: {} (got: '{}', expected: '{}')",
                 i + 1, status, result, test.expected);

        assert_eq!(result, test.expected, "Test {} failed", i + 1);
    }

    println!("\n=== Testing standalone implementation ===");
    for (i, test) in test_cases.iter().enumerate() {
        let result = standalone::smallest_equivalent_string_alt(
            test.s1.to_string(),
            test.s2.to_string(),
            test.base_str.to_string(),
        );

        let status = if result == test.expected { "✓ PASS" } else { "✗ FAIL" };
        println!("Alt Test {}: {} (got: '{}', expected: '{}')",
                 i + 1, status, result, test.expected);

        assert_eq!(result, test.expected, "Alt test {} failed", i + 1);
    }

    println!("\n=== Performance Test ===");
    let large_s1 = "abcdefghijklmnopqrstuvwxyz".repeat(1000);
    let large_s2 = "bcdefghijklmnopqrstuvwxyza".repeat(1000);
    let large_base = "zyxwvutsrqponmlkjihgfedcba".repeat(100);

    let start = std::time::Instant::now();
    let _result = Solution::smallest_equivalent_string(large_s1, large_s2, large_base);
    let duration = start.elapsed();

    println!("Large input processing time: {:?}", duration);
    println!("All tests completed successfully! 🎉");
}

/// LeetCode solution struct (required for LeetCode submission)
struct Solution;

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_basic_cases() {
        assert_eq!(
            Solution::smallest_equivalent_string(
                "parker".to_string(),
                "morris".to_string(),
                "parser".to_string()
            ),
            "makkek"
        );

        assert_eq!(
            Solution::smallest_equivalent_string(
                "hello".to_string(),
                "world".to_string(),
                "hold".to_string()
            ),
            "hdld"
        );
    }

    #[test]
    fn test_edge_cases() {
        // No equivalences
        assert_eq!(
            Solution::smallest_equivalent_string(
                "aa".to_string(),
                "aa".to_string(),
                "abc".to_string()
            ),
            "abc"
        );

        // Empty base string
        assert_eq!(
            Solution::smallest_equivalent_string(
                "ab".to_string(),
                "cd".to_string(),
                "".to_string()
            ),
            ""
        );
    }

    #[test]
    fn test_standalone_implementation() {
        assert_eq!(
            standalone::smallest_equivalent_string_alt(
                "parker".to_string(),
                "morris".to_string(),
                "parser".to_string()
            ),
            "makkek"
        );
    }
}
