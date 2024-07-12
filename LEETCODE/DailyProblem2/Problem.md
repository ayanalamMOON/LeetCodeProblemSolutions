# 1717. Maximum Score From Removing Substrings

`Solved`  
`Medium`

## Topics
- Strings
- Stack
- Greedy Algorithms

## Companies
- [List companies here if any]

## Hint
You are given a string `s` and two integers `x` and `y`. You can perform two types of operations any number of times:

1. **Remove substring "ab" and gain `x` points.**
   - For example, when removing "ab" from "cabxbae" it becomes "cxbae".
2. **Remove substring "ba" and gain `y` points.**
   - For example, when removing "ba" from "cabxbae" it becomes "cabxe".

Return the maximum points you can gain after applying the above operations on `s`.

## Examples

### Example 1
**Input:**
```plaintext
s = "cdbcbbaaabab", x = 4, y = 5
