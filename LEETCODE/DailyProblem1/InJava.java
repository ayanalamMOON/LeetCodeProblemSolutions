import java.util.Stack;

public class Solution {
    public String reverseParentheses(String s) {
        Stack<Character> stack = new Stack<>();
        for (char ch : s.toCharArray()) {
            if (ch == ')') {
                // Start to pop until finding a '('
                StringBuilder sb = new StringBuilder();
                while (!stack.isEmpty() && stack.peek() != '(') {
                    sb.append(stack.pop());
                }
                stack.pop();  // remove the '('
                // Add the reversed substring back to the stack
                for (char reversedChar : sb.toString().toCharArray()) {
                    stack.push(reversedChar);
                }
            } else {
                stack.push(ch);
            }
        }
        // Join the final stack to form the result string
        StringBuilder result = new StringBuilder();
        for (char ch : stack) {
            result.append(ch);
        }
        return result.toString();
    }
}