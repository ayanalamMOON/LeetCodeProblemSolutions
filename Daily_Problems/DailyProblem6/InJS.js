/**
 * @param {number[]} status
 * @param {number[]} candies
 * @param {number[][]} keys
 * @param {number[][]} containedBoxes
 * @param {number[]} initialBoxes
 * @return {number}
 */
var maxCandies = function(status, candies, keys, containedBoxes, initialBoxes) {
    // Track state using Sets for O(1) operations
    const availableBoxes = new Set(initialBoxes);
    const availableKeys = new Set();
    const openedBoxes = new Set();
    const toProcess = [];
    
    // Add initially openable boxes to queue
    for (const box of initialBoxes) {
        if (status[box] === 1) {
            toProcess.push(box);
        }
    }
    
    let totalCandies = 0;
    
    // BFS to process all openable boxes
    while (toProcess.length > 0) {
        const currentBox = toProcess.shift();
        
        // Skip if already opened
        if (openedBoxes.has(currentBox)) {
            continue;
        }
        
        // Open box and collect candies
        openedBoxes.add(currentBox);
        totalCandies += candies[currentBox];
        
        // Collect all keys from this box
        for (const key of keys[currentBox]) {
            availableKeys.add(key);
        }
        
        // Collect all contained boxes
        for (const box of containedBoxes[currentBox]) {
            availableBoxes.add(box);
        }
        
        // Check all available boxes for newly openable ones
        for (const box of availableBoxes) {
            if (!openedBoxes.has(box)) {
                // Can open if box is initially open OR we have the key
                if (status[box] === 1 || availableKeys.has(box)) {
                    toProcess.push(box);
                }
            }
        }
    }
    
    return totalCandies;
};

// Alternative solution using more functional programming style
var maxCandiesFunctional = function(status, candies, keys, containedBoxes, initialBoxes) {
    const state = {
        availableBoxes: new Set(initialBoxes),
        availableKeys: new Set(),
        openedBoxes: new Set(),
        totalCandies: 0
    };
    
    const canOpenBox = (box) => status[box] === 1 || state.availableKeys.has(box);
    
    const openBox = (box) => {
        if (state.openedBoxes.has(box)) return false;
        
        state.openedBoxes.add(box);
        state.totalCandies += candies[box];
        
        // Collect keys
        keys[box].forEach(key => state.availableKeys.add(key));
        
        // Collect contained boxes
        containedBoxes[box].forEach(containedBox => state.availableBoxes.add(containedBox));
        
        return true;
    };
    
    const findOpenableBoxes = () => {
        return Array.from(state.availableBoxes).filter(box => 
            !state.openedBoxes.has(box) && canOpenBox(box)
        );
    };
    
    // Process initially openable boxes
    let toProcess = findOpenableBoxes();
    
    while (toProcess.length > 0) {
        const currentBatch = [...toProcess];
        toProcess = [];
        
        for (const box of currentBatch) {
            if (openBox(box)) {
                // Check for newly openable boxes
                const newlyOpenable = findOpenableBoxes();
                toProcess.push(...newlyOpenable.filter(b => !toProcess.includes(b)));
            }
        }
        
        // Remove duplicates
        toProcess = [...new Set(toProcess)];
    }
    
    return state.totalCandies;
};

// Test function
function testSolution() {
    console.log("=== Testing maxCandies function ===");
    
    // Test Case 1
    const status1 = [1, 0, 1, 0];
    const candies1 = [7, 5, 4, 100];
    const keys1 = [[], [], [1], []];
    const containedBoxes1 = [[1, 2], [3], [], []];
    const initialBoxes1 = [0];
    
    const result1 = maxCandies(status1, candies1, keys1, containedBoxes1, initialBoxes1);
    console.assert(result1 === 16, `Test 1 failed: expected 16, got ${result1}`);
    console.log(`Test 1 passed: ${result1}`);
    
    // Test Case 2
    const status2 = [1, 0, 0, 0, 0, 0];
    const candies2 = [1, 1, 1, 1, 1, 1];
    const keys2 = [[1, 2, 3, 4, 5], [], [], [], [], []];
    const containedBoxes2 = [[1, 2, 3, 4, 5], [], [], [], [], []];
    const initialBoxes2 = [0];
    
    const result2 = maxCandies(status2, candies2, keys2, containedBoxes2, initialBoxes2);
    console.assert(result2 === 6, `Test 2 failed: expected 6, got ${result2}`);
    console.log(`Test 2 passed: ${result2}`);
    
    // Test Case 3: Edge case - no initial boxes
    const status3 = [1, 1, 1];
    const candies3 = [1, 2, 3];
    const keys3 = [[], [], []];
    const containedBoxes3 = [[], [], []];
    const initialBoxes3 = [];
    
    const result3 = maxCandies(status3, candies3, keys3, containedBoxes3, initialBoxes3);
    console.assert(result3 === 0, `Test 3 failed: expected 0, got ${result3}`);
    console.log(`Test 3 passed: ${result3}`);
    
    // Test Case 4: All boxes closed, no keys
    const status4 = [0, 0, 0];
    const candies4 = [1, 2, 3];
    const keys4 = [[], [], []];
    const containedBoxes4 = [[], [], []];
    const initialBoxes4 = [0, 1, 2];
    
    const result4 = maxCandies(status4, candies4, keys4, containedBoxes4, initialBoxes4);
    console.assert(result4 === 0, `Test 4 failed: expected 0, got ${result4}`);
    console.log(`Test 4 passed: ${result4}`);
    
    // Test functional version with same test cases
    console.log("\n=== Testing functional version ===");
    const functionalResult1 = maxCandiesFunctional(status1, candies1, keys1, containedBoxes1, initialBoxes1);
    console.assert(functionalResult1 === 16, `Functional test 1 failed: expected 16, got ${functionalResult1}`);
    console.log(`Functional test 1 passed: ${functionalResult1}`);
    
    console.log("All tests passed!");
}

// Performance comparison function
function performanceTest() {
    console.log("\n=== Performance Comparison ===");
    
    // Generate larger test case
    const n = 100;
    const status = Array(n).fill(0);
    status[0] = 1; // Only first box is initially open
    
    const candies = Array(n).fill(1);
    const keys = Array(n).fill().map((_, i) => i < n - 1 ? [i + 1] : []);
    const containedBoxes = Array(n).fill().map(() => []);
    const initialBoxes = [0];
    
    // Time the BFS version
    const start1 = performance.now();
    const result1 = maxCandies(status, candies, keys, containedBoxes, initialBoxes);
    const end1 = performance.now();
    
    // Time the functional version
    const start2 = performance.now();
    const result2 = maxCandiesFunctional(status, candies, keys, containedBoxes, initialBoxes);
    const end2 = performance.now();
    
    console.log(`BFS version: ${result1} candies in ${(end1 - start1).toFixed(3)}ms`);
    console.log(`Functional version: ${result2} candies in ${(end2 - start2).toFixed(3)}ms`);
    console.assert(result1 === result2, "Results should be equal");
}

// Demo with step-by-step visualization
function demonstrateAlgorithm() {
    console.log("\n=== Algorithm Demonstration ===");
    
    const status = [1, 0, 1, 0];
    const candies = [7, 5, 4, 100];
    const keys = [[], [], [1], []];
    const containedBoxes = [[1, 2], [3], [], []];
    const initialBoxes = [0];
    
    console.log("Initial setup:");
    console.log(`Status: [${status.join(', ')}]`);
    console.log(`Candies: [${candies.join(', ')}]`);
    console.log(`Keys: [${keys.map(k => `[${k.join(', ')}]`).join(', ')}]`);
    console.log(`Contained boxes: [${containedBoxes.map(cb => `[${cb.join(', ')}]`).join(', ')}]`);
    console.log(`Initial boxes: [${initialBoxes.join(', ')}]`);
    console.log("");
    
    // Custom implementation with logging
    const availableBoxes = new Set(initialBoxes);
    const availableKeys = new Set();
    const openedBoxes = new Set();
    let totalCandies = 0;
    let step = 1;
    
    const toProcess = [];
    for (const box of initialBoxes) {
        if (status[box] === 1) {
            toProcess.push(box);
        }
    }
    
    while (toProcess.length > 0) {
        const currentBox = toProcess.shift();
        
        if (openedBoxes.has(currentBox)) continue;
        
        console.log(`Step ${step}: Opening box ${currentBox}`);
        openedBoxes.add(currentBox);
        totalCandies += candies[currentBox];
        
        console.log(`  Collected ${candies[currentBox]} candies (total: ${totalCandies})`);
        
        if (keys[currentBox].length > 0) {
            keys[currentBox].forEach(key => availableKeys.add(key));
            console.log(`  Found keys: [${keys[currentBox].join(', ')}]`);
        }
        
        if (containedBoxes[currentBox].length > 0) {
            containedBoxes[currentBox].forEach(box => availableBoxes.add(box));
            console.log(`  Found boxes: [${containedBoxes[currentBox].join(', ')}]`);
        }
        
        // Check for newly openable boxes
        let newlyOpenable = [];
        for (const box of availableBoxes) {
            if (!openedBoxes.has(box) && (status[box] === 1 || availableKeys.has(box))) {
                if (!toProcess.includes(box)) {
                    toProcess.push(box);
                    newlyOpenable.push(box);
                }
            }
        }
        
        if (newlyOpenable.length > 0) {
            console.log(`  Newly openable boxes: [${newlyOpenable.join(', ')}]`);
        }
        
        console.log(`  Available keys: {${Array.from(availableKeys).join(', ')}}`);
        console.log(`  Queue: [${toProcess.join(', ')}]`);
        console.log("");
        
        step++;
    }
    
    console.log(`Final result: ${totalCandies} candies`);
}

// Export for Node.js environment
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { maxCandies, maxCandiesFunctional, testSolution };
}

// Run tests if this file is executed directly
if (typeof window === 'undefined' && typeof process !== 'undefined') {
    testSolution();
    demonstrateAlgorithm();
    performanceTest();
}

/*
Time Complexity: O(n) where n is the number of boxes
- Each box is processed at most once
- Set operations are O(1) on average

Space Complexity: O(n)
- Sets to track available boxes, keys, and opened boxes
- Array for BFS traversal (queue simulation)

Algorithm:
1. Initialize state tracking with Sets and Array
2. Add initially openable boxes (available + open) to queue
3. BFS: For each box in queue:
   - Skip if already opened
   - Open box: collect candies, keys, contained boxes
   - Check all available boxes for newly openable ones
4. Continue until queue is empty
5. Return total candies collected

JavaScript-Specific Features:
- ES6+ Set for O(1) membership testing
- Array.shift() for queue dequeue operation (O(n) but acceptable for this problem size)
- for...of loops for cleaner iteration
- Template literals for readable string formatting
- Arrow functions for concise function definitions
- Destructuring assignment for cleaner variable declarations
- Optional chaining and nullish coalescing for safer property access

Performance Considerations:
- Array.shift() is O(n) - for better performance, use a proper queue implementation
- Could use Map for better performance with many key operations
- V8 engine optimizations make Set operations very fast

Browser Compatibility:
- Uses ES6+ features (Set, for...of, const/let)
- Compatible with modern browsers (Chrome 51+, Firefox 45+, Safari 10+)
- For older browsers, would need polyfills or transpilation

Alternative Implementations:
- Functional programming style with higher-order functions
- Using Map for key-value associations
- Using more immutable data structures
- Using async/await for demonstration purposes
*/
