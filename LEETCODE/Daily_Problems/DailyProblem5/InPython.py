class Solution:
    def differenceOfSums_bruteforce(self, n: int, m: int) -> int:
        """
        Brute Force Approach - O(n) time, O(1) space
        """
        num1 = 0  # sum of numbers not divisible by m
        num2 = 0  # sum of numbers divisible by m
        
        for i in range(1, n + 1):
            if i % m == 0:
                num2 += i
            else:
                num1 += i
        
        return num1 - num2
    
    def differenceOfSums(self, n: int, m: int) -> int:
        """
        Mathematical Formula Approach - O(1) time, O(1) space
        """
        # Total sum of numbers from 1 to n
        total_sum = n * (n + 1) // 2
        
        # Number of multiples of m in range [1, n]
        multiples_count = n // m
        
        # Sum of multiples of m: m + 2m + 3m + ... + (multiples_count * m)
        # = m * (1 + 2 + 3 + ... + multiples_count)
        # = m * (multiples_count * (multiples_count + 1) // 2)
        num2 = m * multiples_count * (multiples_count + 1) // 2
        
        # Sum of non-multiples = total_sum - sum of multiples
        num1 = total_sum - num2
        
        return num1 - num2
    
    def differenceOfSums_alternative(self, n: int, m: int) -> int:
        """
        Alternative Mathematical Approach - most concise
        """
        total_sum = n * (n + 1) // 2
        multiples_count = n // m
        sum_of_multiples = m * multiples_count * (multiples_count + 1) // 2
        
        # num1 - num2 = (total_sum - sum_of_multiples) - sum_of_multiples
        # = total_sum - 2 * sum_of_multiples
        return total_sum - 2 * sum_of_multiples


def run_tests():
    """Test function to verify all approaches work correctly"""
    solution = Solution()
    
    # Test case 1
    assert solution.differenceOfSums(10, 3) == 19
    assert solution.differenceOfSums_bruteforce(10, 3) == 19
    assert solution.differenceOfSums_alternative(10, 3) == 19
    
    # Test case 2
    assert solution.differenceOfSums(5, 6) == 15
    assert solution.differenceOfSums_bruteforce(5, 6) == 15
    assert solution.differenceOfSums_alternative(5, 6) == 15
    
    # Test case 3
    assert solution.differenceOfSums(5, 1) == -15
    assert solution.differenceOfSums_bruteforce(5, 1) == -15
    assert solution.differenceOfSums_alternative(5, 1) == -15
    
    # Additional test cases
    assert solution.differenceOfSums(1, 2) == 1
    assert solution.differenceOfSums(4, 2) == -2
    assert solution.differenceOfSums(1000, 7) == 84735
    
    print("All test cases passed!")


def demonstrate_solution(n: int, m: int):
    """Function to demonstrate the solution with detailed output"""
    solution = Solution()
    
    print(f"\n=== Solving for n = {n}, m = {m} ===")
    
    # Show brute force approach
    num1 = 0
    num2 = 0
    non_divisible = []
    divisible = []
    
    for i in range(1, n + 1):
        if i % m == 0:
            num2 += i
            divisible.append(i)
        else:
            num1 += i
            non_divisible.append(i)
    
    print(f"Numbers not divisible by {m}: {non_divisible} -> sum = {num1}")
    print(f"Numbers divisible by {m}: {divisible} -> sum = {num2}")
    
    result = solution.differenceOfSums(n, m)
    print(f"Result: {num1} - {num2} = {result}")


def main():
    """Main function"""
    print("LeetCode 2894: Divisible and Non-divisible Sums Difference")
    print("=========================================================")
    
    # Run all test cases
    run_tests()
    
    # Demonstrate with examples
    demonstrate_solution(10, 3)
    demonstrate_solution(5, 6)
    demonstrate_solution(5, 1)
    
    # Interactive input
    print("\n=== Interactive Mode ===")
    try:
        n = int(input("Enter n: "))
        m = int(input("Enter m: "))
        
        solution = Solution()
        result = solution.differenceOfSums(n, m)
        print(f"Result for n={n}, m={m}: {result}")
    except ValueError:
        print("Please enter valid integers!")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")


if __name__ == "__main__":
    main()
