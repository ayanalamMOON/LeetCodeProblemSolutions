# 1061. Lexicographically Smallest Equivalent String

**Difficulty**: Medium
**Topics**: Union Find, String, Array
**Companies**: Premium Lock

## Problem Statement

You are given two strings of the same length `s1` and `s2` and a string `baseStr`.

We say `s1[i]` and `s2[i]` are equivalent characters.

For example, if `s1 = "abc"` and `s2 = "cde"`, then we have `'a' == 'c'`, `'b' == 'd'`, and `'c' == 'e'`.

Equivalent characters follow the usual rules of any equivalence relation:

- **Reflexivity**: `'a' == 'a'`.
- **Symmetry**: `'a' == 'b'` implies `'b' == 'a'`.
- **Transitivity**: `'a' == 'b'` and `'b' == 'c'` implies `'a' == 'c'`.

For example, given the equivalency information from `s1 = "abc"` and `s2 = "cde"`, `"acd"` and `"aab"` are equivalent strings of `baseStr = "eed"`, and `"aab"` is the lexicographically smallest equivalent string of `baseStr`.

Return the lexicographically smallest equivalent string of `baseStr` by using the equivalency information from `s1` and `s2`.

## Examples

### Example 1

```
Input: s1 = "parker", s2 = "morris", baseStr = "parser"
Output: "makkek"
Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [m,p], [a,o], [k,r,s], [e,i].
The characters in each group are equivalent and sorted in lexicographical order.
So the answer is "makkek".
```

### Example 2

```
Input: s1 = "hello", s2 = "world", baseStr = "hold"
Output: "hdld"
Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [h,w], [d,e,o], [l,r].
So only the second letter 'o' in baseStr is changed to 'd', the answer is "hdld".
```

### Example 3

```
Input: s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"
Output: "aauaaaaada"
Explanation: We group the equivalent characters in s1 and s2 as [a,o,e,r,s,c], [l,p], [g,t] and [d,m], thus all letters in baseStr except 'u' and 'd' are transformed to 'a', the answer is "aauaaaaada".
```

## Constraints

- `1 <= s1.length, s2.length, baseStr.length <= 1000`
- `s1.length == s2.length`
- `s1`, `s2`, and `baseStr` consist of lowercase English letters.

## Key Insights

1. **Union Find Pattern**: This problem is a classic application of Union Find (Disjoint Set Union) data structure.
2. **Equivalence Relations**: The problem establishes equivalence classes of characters through transitivity.
3. **Lexicographical Optimization**: Within each equivalence class, we want the lexicographically smallest representative.
4. **Character Mapping**: Build a mapping from each character to its smallest equivalent character.

## Approach

1. **Build Equivalence Relations**: Use Union Find to group equivalent characters from `s1` and `s2`.
2. **Find Representatives**: For each character, find the lexicographically smallest character in its equivalence class.
3. **Transform Base String**: Replace each character in `baseStr` with its smallest equivalent.

## Hints

1. Think about how to efficiently group characters that are equivalent to each other.
2. Consider using Union Find data structure to handle the equivalence relations.
3. How can you ensure that you always pick the lexicographically smallest character from each group?
4. Remember that equivalence is transitive - if a==b and b==c, then a==c.
