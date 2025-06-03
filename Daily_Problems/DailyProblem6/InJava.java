import java.util.*;

class Solution {
    public int maxCandies(int[] status, int[] candies, int[][] keys, 
                         int[][] containedBoxes, int[] initialBoxes) {
        // Track state using HashSets for O(1) operations
        Set<Integer> availableBoxes = new HashSet<>();
        Set<Integer> availableKeys = new HashSet<>();
        Set<Integer> openedBoxes = new HashSet<>();
        Queue<Integer> toProcess = new LinkedList<>();
        
        // Initialize with initial boxes
        for (int box : initialBoxes) {
            availableBoxes.add(box);
            if (status[box] == 1) {
                toProcess.offer(box);
            }
        }
        
        int totalCandies = 0;
        
        // BFS to process all openable boxes
        while (!toProcess.isEmpty()) {
            int currentBox = toProcess.poll();
            
            // Skip if already opened
            if (openedBoxes.contains(currentBox)) {
                continue;
            }
            
            // Open box and collect candies
            openedBoxes.add(currentBox);
            totalCandies += candies[currentBox];
            
            // Collect all keys from this box
            for (int key : keys[currentBox]) {
                availableKeys.add(key);
            }
            
            // Collect all contained boxes
            for (int box : containedBoxes[currentBox]) {
                availableBoxes.add(box);
            }
            
            // Check all available boxes for newly openable ones
            for (int box : availableBoxes) {
                if (!openedBoxes.contains(box)) {
                    // Can open if box is initially open OR we have the key
                    if (status[box] == 1 || availableKeys.contains(box)) {
                        toProcess.offer(box);
                    }
                }
            }
        }
        
        return totalCandies;
    }
}

public class MaxCandiesFromBoxes {
    public static void testSolution() {
        Solution solution = new Solution();
        
        // Test Case 1
        int[] status1 = {1, 0, 1, 0};
        int[] candies1 = {7, 5, 4, 100};
        int[][] keys1 = {{}, {}, {1}, {}};
        int[][] containedBoxes1 = {{1, 2}, {3}, {}, {}};
        int[] initialBoxes1 = {0};
        
        int result1 = solution.maxCandies(status1, candies1, keys1, containedBoxes1, initialBoxes1);
        assert result1 == 16 : "Test 1 failed";
        System.out.println("Test 1 passed: " + result1);
        
        // Test Case 2
        int[] status2 = {1, 0, 0, 0, 0, 0};
        int[] candies2 = {1, 1, 1, 1, 1, 1};
        int[][] keys2 = {{1, 2, 3, 4, 5}, {}, {}, {}, {}, {}};
        int[][] containedBoxes2 = {{1, 2, 3, 4, 5}, {}, {}, {}, {}, {}};
        int[] initialBoxes2 = {0};
        
        int result2 = solution.maxCandies(status2, candies2, keys2, containedBoxes2, initialBoxes2);
        assert result2 == 6 : "Test 2 failed";
        System.out.println("Test 2 passed: " + result2);
        
        // Test Case 3: Edge case - no initial boxes
        int[] status3 = {1, 1, 1};
        int[] candies3 = {1, 2, 3};
        int[][] keys3 = {{}, {}, {}};
        int[][] containedBoxes3 = {{}, {}, {}};
        int[] initialBoxes3 = {};
        
        int result3 = solution.maxCandies(status3, candies3, keys3, containedBoxes3, initialBoxes3);
        assert result3 == 0 : "Test 3 failed";
        System.out.println("Test 3 passed: " + result3);
        
        // Test Case 4: All boxes closed, no keys
        int[] status4 = {0, 0, 0};
        int[] candies4 = {1, 2, 3};
        int[][] keys4 = {{}, {}, {}};
        int[][] containedBoxes4 = {{}, {}, {}};
        int[] initialBoxes4 = {0, 1, 2};
        
        int result4 = solution.maxCandies(status4, candies4, keys4, containedBoxes4, initialBoxes4);
        assert result4 == 0 : "Test 4 failed";
        System.out.println("Test 4 passed: " + result4);
        
        System.out.println("All tests passed!");
    }
    
    public static void main(String[] args) {
        testSolution();
    }
}

/*
Time Complexity: O(n) where n is the number of boxes
- Each box is processed at most once
- HashSet operations are O(1) on average

Space Complexity: O(n)
- HashSets to track available boxes, keys, and opened boxes
- LinkedList queue for BFS traversal

Algorithm:
1. Initialize state tracking with HashSets and LinkedList queue
2. Add initially openable boxes (available + open) to queue
3. BFS: For each box in queue:
   - Skip if already opened
   - Open box: collect candies, keys, contained boxes
   - Check all available boxes for newly openable ones
4. Continue until queue is empty
5. Return total candies collected

Java-Specific Features:
- Uses HashSet for O(1) set operations
- LinkedList implements Queue interface efficiently
- Enhanced for loops for cleaner iteration
- Wrapper Integer class for HashSet operations
- Assert statements for testing (enable with -ea flag)

Memory Management:
- Automatic garbage collection handles memory cleanup
- Collections framework provides optimized data structures
- Autoboxing/unboxing between int and Integer
*/
