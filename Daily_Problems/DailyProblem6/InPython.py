from typing import List
from collections import deque

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], 
                   containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        """
        Find maximum candies that can be collected from boxes.
        
        Args:
            status: List indicating if each box is open (1) or closed (0)
            candies: Number of candies in each box
            keys: List of keys found in each box
            containedBoxes: List of boxes contained in each box
            initialBoxes: Initially available boxes
            
        Returns:
            Maximum number of candies that can be collected
        """
        # Track state using sets for O(1) operations
        available_boxes = set(initialBoxes)
        available_keys = set()
        opened_boxes = set()
        to_process = deque()
        
        # Add initially openable boxes to queue
        for box in initialBoxes:
            if status[box] == 1:
                to_process.append(box)
        
        total_candies = 0
        
        # BFS to process all openable boxes
        while to_process:
            current_box = to_process.popleft()
            
            # Skip if already opened
            if current_box in opened_boxes:
                continue
            
            # Open box and collect candies
            opened_boxes.add(current_box)
            total_candies += candies[current_box]
            
            # Collect all keys from this box
            for key in keys[current_box]:
                available_keys.add(key)
            
            # Collect all contained boxes
            for box in containedBoxes[current_box]:
                available_boxes.add(box)
            
            # Check all available boxes for newly openable ones
            for box in available_boxes:
                if box not in opened_boxes:
                    # Can open if box is initially open OR we have the key
                    if status[box] == 1 or box in available_keys:
                        to_process.append(box)
        
        return total_candies

def test_solution():
    """Test the solution with various test cases."""
    solution = Solution()
    
    # Test Case 1
    status1 = [1, 0, 1, 0]
    candies1 = [7, 5, 4, 100]
    keys1 = [[], [], [1], []]
    containedBoxes1 = [[1, 2], [3], [], []]
    initialBoxes1 = [0]
    
    result1 = solution.maxCandies(status1, candies1, keys1, containedBoxes1, initialBoxes1)
    assert result1 == 16, f"Test 1 failed: expected 16, got {result1}"
    print(f"Test 1 passed: {result1}")
    
    # Test Case 2
    status2 = [1, 0, 0, 0, 0, 0]
    candies2 = [1, 1, 1, 1, 1, 1]
    keys2 = [[1, 2, 3, 4, 5], [], [], [], [], []]
    containedBoxes2 = [[1, 2, 3, 4, 5], [], [], [], [], []]
    initialBoxes2 = [0]
    
    result2 = solution.maxCandies(status2, candies2, keys2, containedBoxes2, initialBoxes2)
    assert result2 == 6, f"Test 2 failed: expected 6, got {result2}"
    print(f"Test 2 passed: {result2}")
    
    # Test Case 3: Edge case - no initial boxes
    status3 = [1, 1, 1]
    candies3 = [1, 2, 3]
    keys3 = [[], [], []]
    containedBoxes3 = [[], [], []]
    initialBoxes3 = []
    
    result3 = solution.maxCandies(status3, candies3, keys3, containedBoxes3, initialBoxes3)
    assert result3 == 0, f"Test 3 failed: expected 0, got {result3}"
    print(f"Test 3 passed: {result3}")
    
    # Test Case 4: All boxes closed, no keys
    status4 = [0, 0, 0]
    candies4 = [1, 2, 3]
    keys4 = [[], [], []]
    containedBoxes4 = [[], [], []]
    initialBoxes4 = [0, 1, 2]
    
    result4 = solution.maxCandies(status4, candies4, keys4, containedBoxes4, initialBoxes4)
    assert result4 == 0, f"Test 4 failed: expected 0, got {result4}"
    print(f"Test 4 passed: {result4}")
    
    # Test Case 5: Single box with key to itself
    status5 = [0]
    candies5 = [5]
    keys5 = [[0]]
    containedBoxes5 = [[]]
    initialBoxes5 = [0]
    
    result5 = solution.maxCandies(status5, candies5, keys5, containedBoxes5, initialBoxes5)
    assert result5 == 0, f"Test 5 failed: expected 0, got {result5}"
    print(f"Test 5 passed: {result5}")
    
    print("All tests passed!")

def demonstrate_algorithm():
    """Demonstrate the algorithm step by step."""
    solution = Solution()
    
    print("=== Algorithm Demonstration ===")
    status = [1, 0, 1, 0]
    candies = [7, 5, 4, 100]
    keys = [[], [], [1], []]
    containedBoxes = [[1, 2], [3], [], []]
    initialBoxes = [0]
    
    print(f"Initial setup:")
    print(f"Status: {status}")
    print(f"Candies: {candies}")
    print(f"Keys: {keys}")
    print(f"Contained boxes: {containedBoxes}")
    print(f"Initial boxes: {initialBoxes}")
    print()
    
    # Simulate step by step
    available_boxes = set(initialBoxes)
    available_keys = set()
    opened_boxes = set()
    total_candies = 0
    step = 1
    
    print(f"Step {step}: Start with box 0 (open)")
    opened_boxes.add(0)
    total_candies += candies[0]
    available_boxes.update(containedBoxes[0])
    print(f"  Opened box 0: +{candies[0]} candies, got boxes {containedBoxes[0]}")
    print(f"  Total candies: {total_candies}")
    print(f"  Available boxes: {available_boxes}")
    print()
    
    step += 1
    print(f"Step {step}: Check available boxes")
    print(f"  Box 1: closed, no key -> skip")
    print(f"  Box 2: open -> process")
    opened_boxes.add(2)
    total_candies += candies[2]
    available_keys.update(keys[2])
    print(f"  Opened box 2: +{candies[2]} candies, got key {keys[2]}")
    print(f"  Total candies: {total_candies}")
    print(f"  Available keys: {available_keys}")
    print()
    
    step += 1
    print(f"Step {step}: Now have key 1, can open box 1")
    opened_boxes.add(1)
    total_candies += candies[1]
    available_boxes.update(containedBoxes[1])
    print(f"  Opened box 1: +{candies[1]} candies, got box {containedBoxes[1]}")
    print(f"  Total candies: {total_candies}")
    print(f"  Available boxes: {available_boxes}")
    print()
    
    step += 1
    print(f"Step {step}: Check box 3")
    print(f"  Box 3: closed, no key 3 -> cannot open")
    print(f"  Final total candies: {total_candies}")
    
    result = solution.maxCandies(status, candies, keys, containedBoxes, initialBoxes)
    print(f"\nActual result: {result}")

if __name__ == "__main__":
    test_solution()
    print()
    demonstrate_algorithm()

"""
Time Complexity: O(n) where n is the number of boxes
- Each box is processed at most once
- Set operations are O(1) on average

Space Complexity: O(n)
- Sets to track available boxes, keys, and opened boxes
- Deque for BFS traversal

Algorithm:
1. Initialize state tracking with sets and deque
2. Add initially openable boxes (available + open) to queue
3. BFS: For each box in queue:
   - Skip if already opened
   - Open box: collect candies, keys, contained boxes
   - Check all available boxes for newly openable ones
4. Continue until queue is empty
5. Return total candies collected

Python-Specific Features:
- Type hints for better code documentation and IDE support
- Sets for O(1) membership testing and updates
- Deque from collections for efficient queue operations
- List comprehensions can be used for functional programming style
- F-strings for readable string formatting
- Docstrings following Google/NumPy style

Key Insights:
- Use BFS to ensure we process boxes as soon as they become available
- Track three types of state: available boxes, collected keys, opened boxes
- A box can be opened if we have it AND (it's initially open OR we have its key)
- Order of opening doesn't affect total candies, only reachability matters

Optimization Opportunities:
- Could use bit manipulation for small n values
- Could cache openability checks if many repeated checks
- Could use more functional programming style with generators
"""
