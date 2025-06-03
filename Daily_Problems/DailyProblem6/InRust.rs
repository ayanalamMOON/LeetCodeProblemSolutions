use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn max_candies(
        status: Vec<i32>, 
        candies: Vec<i32>, 
        keys: Vec<Vec<i32>>, 
        contained_boxes: Vec<Vec<i32>>, 
        initial_boxes: Vec<i32>
    ) -> i32 {
        // Track state using HashSets for O(1) operations
        let mut available_boxes: HashSet<i32> = initial_boxes.iter().cloned().collect();
        let mut available_keys = HashSet::new();
        let mut opened_boxes = HashSet::new();
        let mut to_process = VecDeque::new();
        
        // Add initially openable boxes to queue
        for &box_id in &initial_boxes {
            if status[box_id as usize] == 1 {
                to_process.push_back(box_id);
            }
        }
        
        let mut total_candies = 0;
        
        // BFS to process all openable boxes
        while let Some(current_box) = to_process.pop_front() {
            // Skip if already opened
            if opened_boxes.contains(&current_box) {
                continue;
            }
            
            // Open box and collect candies
            opened_boxes.insert(current_box);
            total_candies += candies[current_box as usize];
            
            // Collect all keys from this box
            for &key in &keys[current_box as usize] {
                available_keys.insert(key);
            }
            
            // Collect all contained boxes
            for &box_id in &contained_boxes[current_box as usize] {
                available_boxes.insert(box_id);
            }
            
            // Check all available boxes for newly openable ones
            for &box_id in &available_boxes {
                if !opened_boxes.contains(&box_id) {
                    // Can open if box is initially open OR we have the key
                    if status[box_id as usize] == 1 || available_keys.contains(&box_id) {
                        to_process.push_back(box_id);
                    }
                }
            }
        }
        
        total_candies
    }
}

// Alternative implementation using more idiomatic Rust patterns
struct BoxState {
    available_boxes: HashSet<i32>,
    available_keys: HashSet<i32>,
    opened_boxes: HashSet<i32>,
    total_candies: i32,
}

impl BoxState {
    fn new(initial_boxes: &[i32]) -> Self {
        Self {
            available_boxes: initial_boxes.iter().cloned().collect(),
            available_keys: HashSet::new(),
            opened_boxes: HashSet::new(),
            total_candies: 0,
        }
    }
    
    fn can_open_box(&self, box_id: i32, status: &[i32]) -> bool {
        !self.opened_boxes.contains(&box_id) && 
        (status[box_id as usize] == 1 || self.available_keys.contains(&box_id))
    }
    
    fn open_box(&mut self, box_id: i32, candies: &[i32], keys: &[Vec<i32>], contained_boxes: &[Vec<i32>]) {
        if self.opened_boxes.contains(&box_id) {
            return;
        }
        
        // Open box and collect candies
        self.opened_boxes.insert(box_id);
        self.total_candies += candies[box_id as usize];
        
        // Collect keys
        for &key in &keys[box_id as usize] {
            self.available_keys.insert(key);
        }
        
        // Collect contained boxes
        for &box_id in &contained_boxes[box_id as usize] {
            self.available_boxes.insert(box_id);
        }
    }
    
    fn find_openable_boxes(&self, status: &[i32]) -> Vec<i32> {
        self.available_boxes
            .iter()
            .filter(|&&box_id| self.can_open_box(box_id, status))
            .cloned()
            .collect()
    }
}

impl Solution {
    pub fn max_candies_idiomatic(
        status: Vec<i32>, 
        candies: Vec<i32>, 
        keys: Vec<Vec<i32>>, 
        contained_boxes: Vec<Vec<i32>>, 
        initial_boxes: Vec<i32>
    ) -> i32 {
        let mut state = BoxState::new(&initial_boxes);
        let mut to_process: VecDeque<i32> = initial_boxes
            .iter()
            .filter(|&&box_id| status[box_id as usize] == 1)
            .cloned()
            .collect();
        
        while let Some(current_box) = to_process.pop_front() {
            if state.opened_boxes.contains(&current_box) {
                continue;
            }
            
            state.open_box(current_box, &candies, &keys, &contained_boxes);
            
            // Add newly openable boxes to queue
            let newly_openable = state.find_openable_boxes(&status);
            for box_id in newly_openable {
                if !to_process.contains(&box_id) {
                    to_process.push_back(box_id);
                }
            }
        }
        
        state.total_candies
    }
}

// For LeetCode submission, we need the struct definition
struct Solution;

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_basic_cases() {
        // Test Case 1
        let status1 = vec![1, 0, 1, 0];
        let candies1 = vec![7, 5, 4, 100];
        let keys1 = vec![vec![], vec![], vec![1], vec![]];
        let contained_boxes1 = vec![vec![1, 2], vec![3], vec![], vec![]];
        let initial_boxes1 = vec![0];
        
        let result1 = Solution::max_candies(status1, candies1, keys1, contained_boxes1, initial_boxes1);
        assert_eq!(result1, 16);
        
        // Test Case 2
        let status2 = vec![1, 0, 0, 0, 0, 0];
        let candies2 = vec![1, 1, 1, 1, 1, 1];
        let keys2 = vec![vec![1, 2, 3, 4, 5], vec![], vec![], vec![], vec![], vec![]];
        let contained_boxes2 = vec![vec![1, 2, 3, 4, 5], vec![], vec![], vec![], vec![], vec![]];
        let initial_boxes2 = vec![0];
        
        let result2 = Solution::max_candies(status2, candies2, keys2, contained_boxes2, initial_boxes2);
        assert_eq!(result2, 6);
    }

    #[test]
    fn test_edge_cases() {
        // Test Case 3: No initial boxes
        let status3 = vec![1, 1, 1];
        let candies3 = vec![1, 2, 3];
        let keys3 = vec![vec![], vec![], vec![]];
        let contained_boxes3 = vec![vec![], vec![], vec![]];
        let initial_boxes3 = vec![];
        
        let result3 = Solution::max_candies(status3, candies3, keys3, contained_boxes3, initial_boxes3);
        assert_eq!(result3, 0);
        
        // Test Case 4: All boxes closed, no keys
        let status4 = vec![0, 0, 0];
        let candies4 = vec![1, 2, 3];
        let keys4 = vec![vec![], vec![], vec![]];
        let contained_boxes4 = vec![vec![], vec![], vec![]];
        let initial_boxes4 = vec![0, 1, 2];
        
        let result4 = Solution::max_candies(status4, candies4, keys4, contained_boxes4, initial_boxes4);
        assert_eq!(result4, 0);
    }

    #[test]
    fn test_idiomatic_version() {
        let status = vec![1, 0, 1, 0];
        let candies = vec![7, 5, 4, 100];
        let keys = vec![vec![], vec![], vec![1], vec![]];
        let contained_boxes = vec![vec![1, 2], vec![3], vec![], vec![]];
        let initial_boxes = vec![0];
        
        let result1 = Solution::max_candies(
            status.clone(), candies.clone(), keys.clone(), 
            contained_boxes.clone(), initial_boxes.clone()
        );
        let result2 = Solution::max_candies_idiomatic(
            status, candies, keys, contained_boxes, initial_boxes
        );
        
        assert_eq!(result1, result2);
        assert_eq!(result1, 16);
    }

    #[test]
    fn test_circular_dependency() {
        // Box 0 has key to box 1, box 1 has key to box 0, both start closed
        let status = vec![0, 0];
        let candies = vec![5, 10];
        let keys = vec![vec![1], vec![0]];
        let contained_boxes = vec![vec![], vec![]];
        let initial_boxes = vec![0, 1];
        
        let result = Solution::max_candies(status, candies, keys, contained_boxes, initial_boxes);
        assert_eq!(result, 0); // Neither can be opened initially
    }

    #[test]
    fn test_self_key() {
        // Box has key to itself but starts closed
        let status = vec![0];
        let candies = vec![5];
        let keys = vec![vec![0]];
        let contained_boxes = vec![vec![]];
        let initial_boxes = vec![0];
        
        let result = Solution::max_candies(status, candies, keys, contained_boxes, initial_boxes);
        assert_eq!(result, 0); // Cannot open itself
    }
}

fn main() {
    println!("Running tests...");
    
    // Example usage
    let status = vec![1, 0, 1, 0];
    let candies = vec![7, 5, 4, 100];
    let keys = vec![vec![], vec![], vec![1], vec![]];
    let contained_boxes = vec![vec![1, 2], vec![3], vec![], vec![]];
    let initial_boxes = vec![0];
    
    let result = Solution::max_candies(status, candies, keys, contained_boxes, initial_boxes);
    println!("Maximum candies: {}", result);
    
    // Run tests
    #[cfg(test)]
    {
        tests::test_basic_cases();
        tests::test_edge_cases();
        tests::test_idiomatic_version();
        tests::test_circular_dependency();
        tests::test_self_key();
        println!("All tests passed!");
    }
}

/*
Time Complexity: O(n) where n is the number of boxes
- Each box is processed at most once
- HashSet operations are O(1) on average

Space Complexity: O(n)
- HashSets to track available boxes, keys, and opened boxes
- VecDeque for BFS traversal

Algorithm:
1. Initialize state tracking with HashSets and VecDeque
2. Add initially openable boxes (available + open) to queue
3. BFS: For each box in queue:
   - Skip if already opened
   - Open box: collect candies, keys, contained boxes
   - Check all available boxes for newly openable ones
4. Continue until queue is empty
5. Return total candies collected

Rust-Specific Features:
- Ownership system ensures memory safety without garbage collection
- Pattern matching with `if let` and `while let` for clean control flow
- Iterator methods like `filter`, `cloned`, `collect` for functional programming
- `snake_case` naming convention following Rust style guide
- Zero-cost abstractions for performance
- Comprehensive error handling capabilities (though not needed here)

Memory Safety:
- Compile-time borrow checking prevents data races and memory leaks
- No null pointer dereferences possible
- Stack allocation by default, heap allocation explicit
- RAII (Resource Acquisition Is Initialization) pattern

Performance Characteristics:
- Zero-cost abstractions mean high-level code compiles to efficient machine code
- No garbage collection pauses
- Predictable performance characteristics
- Memory layout optimizations

Error Handling:
- Result<T, E> type for recoverable errors
- Option<T> type for nullable values
- Panic for unrecoverable errors (used sparingly)

Testing:
- Built-in testing framework with #[test] attribute
- Unit tests in the same file or separate test modules
- Integration tests in separate files
- Comprehensive assertion macros

Key Insights:
- Use BFS to ensure we process boxes as soon as they become available
- Track three types of state: available boxes, collected keys, opened boxes
- A box can be opened if we have it AND (it's initially open OR we have its key)
- Order of opening doesn't affect total candies, only reachability matters

Rust Best Practices Demonstrated:
- Use of standard collections (HashSet, VecDeque)
- Proper error handling patterns
- Memory-efficient data structures
- Clear separation of concerns with struct methods
- Comprehensive testing coverage
*/
