"""
@file InPython.py
@brief LeetCode 1061: Lexicographically Smallest Equivalent String
@author LeetCode Problem Solutions
@date 2024

Problem: Given two strings s1 and s2 of same length and a string baseStr,
find the lexicographically smallest equivalent string of baseStr using
character equivalence relationships from s1 and s2.

Approach: Union Find with Path Compression
- Use Union Find to manage character equivalence classes
- Always make lexicographically smaller character the root
- Apply path compression for optimal performance

Time Complexity: O(α(26) × (|s1| + |baseStr|)) ≈ O(|s1| + |baseStr|)
Space Complexity: O(26) = O(1)
"""

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        """
        Find lexicographically smallest equivalent string
        
        Args:
            s1: First equivalence string
            s2: Second equivalence string
            baseStr: Base string to transform
            
        Returns:
            Lexicographically smallest equivalent string
        """
        # Initialize Union Find structure - each character is its own parent
        parent = list(range(26))
        
        def find(x: int) -> int:
            """
            Find operation with path compression
            
            Args:
                x: Character index (0-25 for 'a'-'z')
                
            Returns:
                Root representative of x's equivalence class
            """
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        def unite(x: int, y: int) -> None:
            """
            Union operation with lexicographical preference
            
            Args:
                x: First character index
                y: Second character index
            """
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                # Always make smaller character the root for lexicographical order
                if rootX < rootY:
                    parent[rootY] = rootX
                else:
                    parent[rootX] = rootY
        
        # Build equivalence relationships
        for c1, c2 in zip(s1, s2):
            unite(ord(c1) - ord('a'), ord(c2) - ord('a'))
        
        # Transform baseStr using equivalence mappings
        result = []
        for c in baseStr:
            char_idx = ord(c) - ord('a')
            root_idx = find(char_idx)
            result.append(chr(ord('a') + root_idx))
        
        return ''.join(result)


def main():
    """Test driver function"""
    solution = Solution()
    
    # Test Case 1
    s1_1, s2_1, baseStr_1 = "parker", "morris", "parser"
    result_1 = solution.smallestEquivalentString(s1_1, s2_1, baseStr_1)
    print(f"Test 1: {result_1}")
    # Expected: "makkek"
    
    # Test Case 2
    s1_2, s2_2, baseStr_2 = "hello", "world", "hold"
    result_2 = solution.smallestEquivalentString(s1_2, s2_2, baseStr_2)
    print(f"Test 2: {result_2}")
    # Expected: "hdld"
    
    # Test Case 3
    s1_3, s2_3, baseStr_3 = "leetcode", "programs", "sourcecode"
    result_3 = solution.smallestEquivalentString(s1_3, s2_3, baseStr_3)
    print(f"Test 3: {result_3}")
    # Expected: "aauaaaaada"
    
    # Edge Case: No equivalences
    s1_4, s2_4, baseStr_4 = "aa", "aa", "abc"
    result_4 = solution.smallestEquivalentString(s1_4, s2_4, baseStr_4)
    print(f"Test 4: {result_4}")
    # Expected: "abc"
    
    # Performance test with edge cases
    test_cases = [
        # All characters map to 'a'
        ("abc", "aaa", "xyz", "aaa"),
        # Single character
        ("a", "b", "c", "a"),
        # Empty base string (edge case)
        ("ab", "cd", "", ""),
        # Long transitive chain
        ("abcdefg", "bcdefgh", "ghijklm", "aaaaaaa"),
    ]
    
    for i, (s1, s2, baseStr, expected) in enumerate(test_cases, 5):
        result = solution.smallestEquivalentString(s1, s2, baseStr)
        print(f"Test {i}: {result} (expected: {expected})")
        assert result == expected, f"Test {i} failed: got {result}, expected {expected}"
    
    print("All tests passed!")


if __name__ == "__main__":
    main()
