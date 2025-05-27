# 1639. Number of Ways to Form a Target String Given a Dictionary

**Difficulty:** Hard  
**Topics:** Dynamic Programming, String  
**Companies:** Premium Lock  

## Problem Statement

You are given a list of strings of the same length `words` and a string `target`.

Your task is to form `target` using the given words under the following rules:

1. `target` should be formed from left to right.
2. To form the `ith` character (0-indexed) of `target`, you can choose the `kth` character of the `jth` string in `words` if `target[i] = words[j][k]`.
3. Once you use the `kth` character of the `jth` string of `words`, you can no longer use the `xth` character of any string in `words` where `x <= k`. In other words, all characters to the left of or at index `k` become unusable for every string.
4. Repeat the process until you form the string `target`.

Notice that you can use multiple characters from the same string in `words` provided the conditions above are met.

Return the number of ways to form `target` from `words`. Since the answer may be too large, return it modulo `10^9 + 7`.

## Examples

### Example 1:
```
Input: words = ["acca","bbbb","caca"], target = "aba"
Output: 6
Explanation: There are 6 ways to form target.
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")
```

### Example 2:
```
Input: words = ["abba","baab"], target = "bab"
Output: 4
Explanation: There are 4 ways to form target.
"bab" -> index 0 ("baab"), index 1 ("baab"), index 2 ("abba")
"bab" -> index 0 ("baab"), index 1 ("baab"), index 3 ("baab")
"bab" -> index 0 ("baab"), index 2 ("baab"), index 3 ("baab")
"bab" -> index 1 ("abba"), index 2 ("baab"), index 3 ("baab")
```

## Constraints

- `1 <= words.length <= 1000`
- `1 <= words[i].length <= 1000`
- All strings in `words` have the same length.
- `1 <= target.length <= 1000`
- `words[i]` and `target` contain only lowercase English letters.

## Key Insights

1. **Dynamic Programming Problem**: We need to count the number of ways, which suggests DP.
2. **Character Frequency**: For each position in words, we need to count how many times each character appears.
3. **Position Constraint**: Once we use position k, we can't use positions 0 to k in any subsequent choices.
4. **Left-to-Right Formation**: We must form the target string from left to right.

## Approach

1. **Precompute character frequencies** at each position across all words.
2. **Use DP** where `dp[i][j]` represents the number of ways to form the first `i` characters of target using the first `j` positions from words.
3. **Transition**: For each character in target, either skip the current position in words or use it if it matches.
4. **Base Case**: `dp[0][j] = 1` for all j (empty target can be formed in 1 way).
5. **Final Answer**: `dp[target.length()][words[0].length()]`
