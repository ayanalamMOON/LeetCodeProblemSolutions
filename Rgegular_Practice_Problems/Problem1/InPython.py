from typing import List
from functools import lru_cache

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        """
        2D Dynamic Programming Approach
        """
        MOD = 1000000007
        m = len(target)
        n = len(words[0])
        
        if m > n:
            return 0
        
        # Precompute character frequencies at each position
        freq = [[0] * 26 for _ in range(n)]
        for word in words:
            for i, char in enumerate(word):
                freq[i][ord(char) - ord('a')] += 1
        
        # DP table: dp[i][j] = ways to form first i chars using first j positions
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base case: empty target can be formed in 1 way
        for j in range(n + 1):
            dp[0][j] = 1
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Skip current position
                dp[i][j] = dp[i][j-1]
                
                # Use current position if character matches
                char_index = ord(target[i-1]) - ord('a')
                if freq[j-1][char_index] > 0:
                    dp[i][j] = (dp[i][j] + dp[i-1][j-1] * freq[j-1][char_index]) % MOD
        
        return dp[m][n]
    
    def numWaysOptimized(self, words: List[str], target: str) -> int:
        """
        Space Optimized 1D DP
        """
        MOD = 1000000007
        m = len(target)
        n = len(words[0])
        
        if m > n:
            return 0
        
        # Precompute frequencies
        freq = [[0] * 26 for _ in range(n)]
        for word in words:
            for i, char in enumerate(word):
                freq[i][ord(char) - ord('a')] += 1
        
        # Space optimized DP
        prev = [1] * (n + 1)
        curr = [0] * (n + 1)
        
        for i in range(1, m + 1):
            curr[0] = 0
            for j in range(1, n + 1):
                curr[j] = curr[j-1]
                
                char_index = ord(target[i-1]) - ord('a')
                if freq[j-1][char_index] > 0:
                    curr[j] = (curr[j] + prev[j-1] * freq[j-1][char_index]) % MOD
            
            prev, curr = curr, [0] * (n + 1)
        
        return prev[n]
    
    def numWaysMemo(self, words: List[str], target: str) -> int:
        """
        Memoized Recursion (Top-Down DP)
        """
        MOD = 1000000007
        m = len(target)
        n = len(words[0])
        
        if m > n:
            return 0
        
        # Precompute frequencies
        freq = [[0] * 26 for _ in range(n)]
        for word in words:
            for i, char in enumerate(word):
                freq[i][ord(char) - ord('a')] += 1
        
        @lru_cache(maxsize=None)
        def dfs(target_idx: int, word_pos: int) -> int:
            # Base cases
            if target_idx == m:
                return 1
            if word_pos == n:
                return 0
            if n - word_pos < m - target_idx:
                return 0
            
            # Skip current position
            result = dfs(target_idx, word_pos + 1)
            
            # Use current position
            char_index = ord(target[target_idx]) - ord('a')
            if freq[word_pos][char_index] > 0:
                result = (result + dfs(target_idx + 1, word_pos + 1) * freq[word_pos][char_index]) % MOD
            
            return result
        
        return dfs(0, 0)
    
    def numWaysPythonic(self, words: List[str], target: str) -> int:
        """
        More Pythonic approach using collections.Counter
        """
        from collections import Counter
        
        MOD = 1000000007
        m = len(target)
        n = len(words[0])
        
        if m > n:
            return 0
        
        # Use Counter for more Pythonic frequency counting
        freq = [Counter() for _ in range(n)]
        for word in words:
            for i, char in enumerate(word):
                freq[i][char] += 1
        
        # DP with defaultdict for cleaner code
        from collections import defaultdict
        dp = defaultdict(int)
        
        # Base case
        for j in range(n + 1):
            dp[(0, j)] = 1
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[(i, j)] = dp[(i, j-1)]
                
                if target[i-1] in freq[j-1]:
                    dp[(i, j)] = (dp[(i, j)] + dp[(i-1, j-1)] * freq[j-1][target[i-1]]) % MOD
        
        return dp[(m, n)]


def run_tests():
    """Test function to verify all approaches work correctly"""
    solution = Solution()
    
    # Test case 1
    words1 = ["acca", "bbbb", "caca"]
    target1 = "aba"
    assert solution.numWays(words1, target1) == 6
    assert solution.numWaysOptimized(words1, target1) == 6
    assert solution.numWaysMemo(words1, target1) == 6
    assert solution.numWaysPythonic(words1, target1) == 6
    
    # Test case 2
    words2 = ["abba", "baab"]
    target2 = "bab"
    assert solution.numWays(words2, target2) == 4
    assert solution.numWaysOptimized(words2, target2) == 4
    assert solution.numWaysMemo(words2, target2) == 4
    assert solution.numWaysPythonic(words2, target2) == 4
    
    # Edge cases
    words3 = ["a", "b"]
    target3 = "ab"
    assert solution.numWays(words3, target3) == 1
    
    words4 = ["abc"]
    target4 = "abcd"
    assert solution.numWays(words4, target4) == 0
    
    print("All Python test cases passed!")


def demonstrate_solution(words: List[str], target: str):
    """Function to demonstrate the solution with detailed output"""
    solution = Solution()
    
    print(f"\n=== Python Analysis: words = {words}, target = \"{target}\" ===")
    
    # Show character frequency analysis
    n = len(words[0])
    freq = [[0] * 26 for _ in range(n)]
    for word in words:
        for i, char in enumerate(word):
            freq[i][ord(char) - ord('a')] += 1
    
    print("Character frequency at each position:")
    for i in range(n):
        print(f"Position {i}: ", end="")
        for j in range(26):
            if freq[i][j] > 0:
                print(f"{chr(ord('a') + j)}={freq[i][j]} ", end="")
        print()
    
    result = solution.numWays(words, target)
    print(f"Number of ways: {result}")


def performance_comparison():
    """Compare performance of different approaches"""
    import time
    
    solution = Solution()
    words = ["acca", "bbbb", "caca"] * 100  # Larger test case
    target = "aba" * 50
    
    # Test different approaches
    approaches = [
        ("2D DP", solution.numWays),
        ("Optimized 1D", solution.numWaysOptimized),
        ("Memoized", solution.numWaysMemo),
        ("Pythonic", solution.numWaysPythonic)
    ]
    
    print("\n=== Performance Comparison ===")
    for name, method in approaches:
        start_time = time.time()
        try:
            result = method(words[:3], "aba")  # Use smaller case for demo
            end_time = time.time()
            print(f"{name}: {result} (Time: {end_time - start_time:.6f}s)")
        except Exception as e:
            print(f"{name}: Error - {e}")


def main():
    """Main function"""
    print("LeetCode 1639: Target String Formation - Python Solution")
    print("=======================================================")
    
    # Run tests
    run_tests()
    
    # Demonstrate examples
    words1 = ["acca", "bbbb", "caca"]
    target1 = "aba"
    demonstrate_solution(words1, target1)
    
    words2 = ["abba", "baab"]
    target2 = "bab"
    demonstrate_solution(words2, target2)
    
    # Performance comparison
    performance_comparison()
    
    # Interactive mode
    print("\n=== Interactive Mode ===")
    try:
        num_words = int(input("Enter number of words: "))
        words = []
        print(f"Enter {num_words} words:")
        for i in range(num_words):
            word = input(f"Word {i+1}: ").strip()
            words.append(word)
        
        target = input("Enter target string: ").strip()
        
        solution = Solution()
        result = solution.numWays(words, target)
        print(f"Number of ways: {result}")
        
    except (ValueError, KeyboardInterrupt):
        print("Invalid input or interrupted by user.")


if __name__ == "__main__":
    main()
