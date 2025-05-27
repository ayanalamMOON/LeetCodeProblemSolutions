# 🔧 Language-Specific Implementation Guide

This guide provides detailed information about implementing LeetCode solutions in each supported programming language, including setup, conventions, optimizations, and best practices.

## 📋 Table of Contents

- [C++ Implementation Guide](#cpp-implementation-guide)
- [Java Implementation Guide](#java-implementation-guide)
- [Python Implementation Guide](#python-implementation-guide)
- [JavaScript Implementation Guide](#javascript-implementation-guide)
- [Rust Implementation Guide](#rust-implementation-guide)
- [Cross-Language Patterns](#cross-language-patterns)
- [Performance Optimization Tips](#performance-optimization-tips)

## 🏃 C++ Implementation Guide

### Environment Setup
```bash
# Install GCC (recommended version 9+)
sudo apt-get install g++ gcc

# Install Clang (alternative compiler)
sudo apt-get install clang

# Verification
g++ --version
clang++ --version
```

### Compilation Commands
```bash
# Development build
g++ -std=c++17 -Wall -Wextra -g solution.cpp -o solution

# Optimized build (for performance testing)
g++ -std=c++17 -O2 -DNDEBUG solution.cpp -o solution

# Debug build with all warnings
g++ -std=c++17 -Wall -Wextra -Wpedantic -g -fsanitize=address solution.cpp -o solution
```

### Code Structure Template
```cpp
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <climits>
#include <iostream>
#include <cassert>

using namespace std;

class Solution {
public:
    // Main solution function
    int solutionFunction(vector<int>& nums, int target) {
        // Implementation here
        return result;
    }
    
private:
    // Helper functions if needed
    bool isValid(int value) {
        return value >= 0;
    }
};

// Testing framework
void runTests() {
    Solution sol;
    
    // Test case 1
    vector<int> nums1 = {1, 2, 3, 4, 5};
    assert(sol.solutionFunction(nums1, 3) == expected_result);
    
    // Test case 2 - edge case
    vector<int> nums2 = {};
    assert(sol.solutionFunction(nums2, 0) == expected_result);
    
    cout << "All tests passed!" << endl;
}

int main() {
    runTests();
    
    // Interactive testing
    Solution sol;
    vector<int> nums = {1, 2, 3, 4, 5};
    int result = sol.solutionFunction(nums, 3);
    cout << "Result: " << result << endl;
    
    return 0;
}
```

### C++ Best Practices
1. **Use STL containers and algorithms**: `vector`, `unordered_map`, `sort`, `binary_search`
2. **Pass by reference**: Use `const vector<int>&` for read-only parameters
3. **Memory management**: Prefer smart pointers over raw pointers
4. **Const correctness**: Mark functions and variables `const` when possible
5. **Use auto**: Let compiler deduce types for complex iterators

### Performance Optimizations
```cpp
// 1. Reserve vector capacity when size is known
vector<int> result;
result.reserve(n);

// 2. Use unordered containers for O(1) lookup
unordered_map<int, int> freq;
unordered_set<int> seen;

// 3. Avoid unnecessary copies
for (const auto& item : container) { /* ... */ }

// 4. Use move semantics
return std::move(result);

// 5. Prefer range-based loops
for (int num : nums) { /* ... */ }
```

## ☕ Java Implementation Guide

### Environment Setup
```bash
# Install OpenJDK
sudo apt-get install openjdk-11-jdk

# Verification
java -version
javac -version
```

### Compilation and Execution
```bash
# Compile
javac Solution.java

# Run
java Solution

# With classpath (if using packages)
javac -cp . com/leetcode/Solution.java
java -cp . com.leetcode.Solution
```

### Code Structure Template
```java
import java.util.*;

public class Solution {
    
    // Main solution function
    public int solutionFunction(int[] nums, int target) {
        // Implementation here
        return result;
    }
    
    // Helper method
    private boolean isValid(int value) {
        return value >= 0;
    }
    
    // Testing framework
    public static void runTests() {
        Solution sol = new Solution();
        
        // Test case 1
        int[] nums1 = {1, 2, 3, 4, 5};
        assert sol.solutionFunction(nums1, 3) == expected_result;
        
        // Test case 2 - edge case
        int[] nums2 = {};
        assert sol.solutionFunction(nums2, 0) == expected_result;
        
        System.out.println("All tests passed!");
    }
    
    public static void main(String[] args) {
        runTests();
        
        // Interactive testing
        Solution sol = new Solution();
        int[] nums = {1, 2, 3, 4, 5};
        int result = sol.solutionFunction(nums, 3);
        System.out.println("Result: " + result);
    }
}
```

### Java Best Practices
1. **Use appropriate collections**: `ArrayList`, `HashMap`, `HashSet`, `PriorityQueue`
2. **StringBuilder for string operations**: Avoid string concatenation in loops
3. **Stream API**: Use for functional programming patterns
4. **Generics**: Provide type safety with `List<Integer>`, `Map<String, Integer>`
5. **Exception handling**: Use try-catch for error-prone operations

### Performance Optimizations
```java
// 1. Initialize collections with capacity
List<Integer> result = new ArrayList<>(n);
Map<Integer, Integer> freq = new HashMap<>(n);

// 2. Use primitive arrays when possible
int[] nums = new int[n];  // instead of Integer[]

// 3. StringBuilder for string building
StringBuilder sb = new StringBuilder();
sb.append(value);

// 4. Use enhanced for loops
for (int num : nums) { /* ... */ }

// 5. Stream operations for complex transformations
List<Integer> filtered = nums.stream()
    .filter(x -> x > 0)
    .collect(Collectors.toList());
```

## 🐍 Python Implementation Guide

### Environment Setup
```bash
# Install Python 3.8+
sudo apt-get install python3 python3-pip

# Install type checking (optional)
pip3 install mypy

# Verification
python3 --version
pip3 --version
```

### Code Structure Template
```python
from typing import List, Dict, Set, Optional
import unittest

class Solution:
    def solution_function(self, nums: List[int], target: int) -> int:
        """
        Brief description of the solution approach.
        
        Args:
            nums: List of integers
            target: Target value
            
        Returns:
            Integer result
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Implementation here
        return result
    
    def _is_valid(self, value: int) -> bool:
        """Helper method with underscore prefix for private methods."""
        return value >= 0

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    
    def test_basic_case(self):
        nums = [1, 2, 3, 4, 5]
        result = self.sol.solution_function(nums, 3)
        self.assertEqual(result, expected_result)
    
    def test_edge_case(self):
        nums = []
        result = self.sol.solution_function(nums, 0)
        self.assertEqual(result, expected_result)
    
    def test_large_input(self):
        nums = list(range(10000))
        result = self.sol.solution_function(nums, 5000)
        self.assertIsInstance(result, int)

def interactive_test():
    """Interactive testing function."""
    sol = Solution()
    nums = [1, 2, 3, 4, 5]
    result = sol.solution_function(nums, 3)
    print(f"Result: {result}")

if __name__ == "__main__":
    # Run unit tests
    unittest.main(argv=[''], exit=False, verbosity=2)
    
    # Run interactive test
    interactive_test()
```

### Python Best Practices
1. **Type hints**: Use `typing` module for better code documentation
2. **List comprehensions**: Use for concise and readable operations
3. **Built-in functions**: Leverage `sum`, `max`, `min`, `sorted`, `enumerate`
4. **Context managers**: Use `with` statements for resource management
5. **Docstrings**: Document functions with proper docstrings

### Performance Optimizations
```python
# 1. Use list comprehensions instead of loops
result = [x * 2 for x in nums if x > 0]

# 2. Use collections module for specialized data structures
from collections import defaultdict, Counter, deque
freq = Counter(nums)
graph = defaultdict(list)

# 3. Use set for O(1) lookups
seen = set()
unique_nums = set(nums)

# 4. Generator expressions for memory efficiency
total = sum(x * 2 for x in nums if x > 0)

# 5. Use enumerate instead of range(len())
for i, num in enumerate(nums):
    # Process index and value
```

## 🌐 JavaScript Implementation Guide

### Environment Setup
```bash
# Install Node.js
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

# Verification
node --version
npm --version
```

### Code Structure Template
```javascript
/**
 * Main solution function
 * @param {number[]} nums - Array of integers
 * @param {number} target - Target value
 * @return {number} Result
 */
var solutionFunction = function(nums, target) {
    // Implementation here
    return result;
};

/**
 * Helper function
 * @param {number} value
 * @return {boolean}
 */
const isValid = (value) => {
    return value >= 0;
};

// Testing framework
function runTests() {
    // Test case 1
    const nums1 = [1, 2, 3, 4, 5];
    console.assert(solutionFunction(nums1, 3) === expected_result, 'Test 1 failed');
    
    // Test case 2 - edge case
    const nums2 = [];
    console.assert(solutionFunction(nums2, 0) === expected_result, 'Test 2 failed');
    
    console.log('All tests passed!');
}

// Performance testing
function performanceTest() {
    const start = performance.now();
    
    const largeNums = Array.from({length: 100000}, (_, i) => i);
    const result = solutionFunction(largeNums, 50000);
    
    const end = performance.now();
    console.log(`Performance test completed in ${end - start} milliseconds`);
    console.log(`Result: ${result}`);
}

// Interactive testing
function interactiveTest() {
    const nums = [1, 2, 3, 4, 5];
    const result = solutionFunction(nums, 3);
    console.log(`Result: ${result}`);
}

// Run all tests
if (require.main === module) {
    runTests();
    performanceTest();
    interactiveTest();
}

// Export for use in other modules
module.exports = { solutionFunction, isValid };
```

### JavaScript Best Practices
1. **Use const/let**: Avoid `var` for better scoping
2. **Arrow functions**: Use for concise function expressions
3. **Destructuring**: Extract values from arrays and objects efficiently
4. **Template literals**: Use backticks for string interpolation
5. **Modern array methods**: `map`, `filter`, `reduce`, `find`, `some`, `every`

### Performance Optimizations
```javascript
// 1. Use Map for O(1) key-value operations
const freq = new Map();
freq.set(key, value);

// 2. Use Set for O(1) lookups
const seen = new Set();
seen.has(value);

// 3. Use typed arrays for numerical computations
const nums = new Int32Array(n);

// 4. Avoid array methods in performance-critical sections
// Instead of: nums.filter(x => x > 0).map(x => x * 2)
// Use: for loop with manual filtering and mapping

// 5. Use array initialization patterns
const result = Array(n).fill(0);
const matrix = Array(m).fill().map(() => Array(n).fill(0));
```

## 🦀 Rust Implementation Guide

### Environment Setup
```bash
# Install Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source ~/.cargo/env

# Update Rust
rustup update

# Verification
rustc --version
cargo --version
```

### Project Structure (Optional)
```bash
# Create new Cargo project
cargo new leetcode_solution
cd leetcode_solution

# Add to Cargo.toml for testing
[dev-dependencies]
criterion = "0.4"
```

### Code Structure Template
```rust
use std::collections::{HashMap, HashSet};

impl Solution {
    /// Main solution function
    /// 
    /// # Arguments
    /// * `nums` - Vector of integers
    /// * `target` - Target value
    /// 
    /// # Returns
    /// * Integer result
    /// 
    /// # Time Complexity
    /// O(n)
    /// 
    /// # Space Complexity
    /// O(1)
    pub fn solution_function(nums: Vec<i32>, target: i32) -> i32 {
        // Implementation here
        result
    }
    
    /// Helper function
    fn is_valid(value: i32) -> bool {
        value >= 0
    }
}

// Define Solution struct for LeetCode compatibility
struct Solution;

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_basic_case() {
        let nums = vec![1, 2, 3, 4, 5];
        let result = Solution::solution_function(nums, 3);
        assert_eq!(result, expected_result);
    }
    
    #[test]
    fn test_edge_case() {
        let nums = vec![];
        let result = Solution::solution_function(nums, 0);
        assert_eq!(result, expected_result);
    }
    
    #[test]
    fn test_large_input() {
        let nums: Vec<i32> = (0..100000).collect();
        let result = Solution::solution_function(nums, 50000);
        assert!(result >= 0); // Basic sanity check
    }
}

fn main() {
    // Interactive testing
    let nums = vec![1, 2, 3, 4, 5];
    let result = Solution::solution_function(nums, 3);
    println!("Result: {}", result);
    
    // Performance testing
    let start = std::time::Instant::now();
    let large_nums: Vec<i32> = (0..100000).collect();
    let result = Solution::solution_function(large_nums, 50000);
    let duration = start.elapsed();
    println!("Performance test: {} in {:?}", result, duration);
}
```

### Rust Best Practices
1. **Ownership and borrowing**: Understand when to use `&`, `&mut`, and owned values
2. **Pattern matching**: Use `match` and `if let` for control flow
3. **Error handling**: Use `Result<T, E>` and `Option<T>` appropriately
4. **Iterators**: Leverage Rust's powerful iterator system
5. **Traits**: Implement and use traits for generic programming

### Performance Optimizations
```rust
// 1. Use HashMap and HashSet for O(1) operations
use std::collections::{HashMap, HashSet};
let mut freq: HashMap<i32, i32> = HashMap::new();
let mut seen: HashSet<i32> = HashSet::new();

// 2. Pre-allocate collections when size is known
let mut result = Vec::with_capacity(n);
let mut map = HashMap::with_capacity(n);

// 3. Use iterators for functional programming
let result: Vec<i32> = nums.iter()
    .filter(|&&x| x > 0)
    .map(|&x| x * 2)
    .collect();

// 4. Avoid unnecessary allocations
fn process_slice(nums: &[i32]) -> i32 {
    // Work with slice instead of owned Vec
}

// 5. Use appropriate integer types
use std::collections::HashMap;
let mut freq: HashMap<i32, usize> = HashMap::new();
```

## 🔄 Cross-Language Patterns

### Common Algorithmic Patterns

#### Two Pointers
```cpp
// C++
int left = 0, right = nums.size() - 1;
while (left < right) {
    // Process and move pointers
}
```

```java
// Java
int left = 0, right = nums.length - 1;
while (left < right) {
    // Process and move pointers
}
```

```python
# Python
left, right = 0, len(nums) - 1
while left < right:
    # Process and move pointers
```

```javascript
// JavaScript
let left = 0, right = nums.length - 1;
while (left < right) {
    // Process and move pointers
}
```

```rust
// Rust
let mut left = 0;
let mut right = nums.len() - 1;
while left < right {
    // Process and move pointers
}
```

#### Sliding Window
```cpp
// C++ - Fixed size window
int windowSum = 0;
for (int i = 0; i < k; i++) {
    windowSum += nums[i];
}
int maxSum = windowSum;
for (int i = k; i < nums.size(); i++) {
    windowSum += nums[i] - nums[i - k];
    maxSum = max(maxSum, windowSum);
}
```

```python
# Python - Variable size window
left = 0
current_sum = 0
max_length = 0

for right in range(len(nums)):
    current_sum += nums[right]
    
    while current_sum > target:
        current_sum -= nums[left]
        left += 1
    
    max_length = max(max_length, right - left + 1)
```

#### Hash Table Frequency Counting
```java
// Java
Map<Integer, Integer> freq = new HashMap<>();
for (int num : nums) {
    freq.put(num, freq.getOrDefault(num, 0) + 1);
}
```

```python
# Python
from collections import Counter
freq = Counter(nums)
# or
freq = {}
for num in nums:
    freq[num] = freq.get(num, 0) + 1
```

```javascript
// JavaScript
const freq = new Map();
for (const num of nums) {
    freq.set(num, (freq.get(num) || 0) + 1);
}
```

```rust
// Rust
use std::collections::HashMap;
let mut freq: HashMap<i32, i32> = HashMap::new();
for &num in &nums {
    *freq.entry(num).or_insert(0) += 1;
}
```

## ⚡ Performance Optimization Tips

### General Optimization Principles
1. **Algorithm first**: Choose the optimal algorithm before micro-optimizations
2. **Data structure selection**: Use appropriate data structures for the problem
3. **Memory access patterns**: Consider cache-friendly access patterns
4. **Early termination**: Add conditions to exit early when possible
5. **Avoid unnecessary work**: Skip redundant calculations

### Language-Specific Performance Tips

#### C++
- Use `vector::reserve()` when size is known
- Prefer `++i` over `i++` in loops
- Use `std::move` for expensive-to-copy objects
- Consider `std::unordered_map` over `std::map` for O(1) access
- Use range-based for loops when possible

#### Java
- Initialize collections with appropriate capacity
- Use primitive arrays instead of wrapper classes when possible
- StringBuilder for string concatenation in loops
- Stream API can be slower than traditional loops for simple operations
- Consider using `ArrayList` over `LinkedList` for most cases

#### Python
- List comprehensions are generally faster than loops
- Use `set` for membership testing instead of `list`
- `collections.deque` for O(1) append/pop from both ends
- NumPy for numerical computations with large datasets
- Consider using `slots` for classes with many instances

#### JavaScript
- Use `Map` and `Set` for better performance than plain objects
- Typed arrays for numerical computations
- Avoid frequent DOM manipulation in web contexts
- Use `Object.hasOwnProperty()` for safe property checking
- Consider using `for...of` loops for better readability

#### Rust
- Use iterators for functional programming patterns
- `Vec::with_capacity()` for pre-allocation
- Consider using `&str` instead of `String` when possible
- Use `HashMap::with_capacity()` for better performance
- Leverage zero-cost abstractions

### Profiling and Benchmarking
Each language provides tools for performance analysis:
- **C++**: Valgrind, gprof, perf
- **Java**: JProfiler, VisualVM, built-in JVM profiling
- **Python**: cProfile, line_profiler, memory_profiler
- **JavaScript**: Chrome DevTools, Node.js profiler
- **Rust**: cargo-flamegraph, criterion for benchmarking

---

This guide provides a solid foundation for implementing efficient LeetCode solutions across all supported languages. Remember that the best solution often depends on the specific problem constraints and requirements!
