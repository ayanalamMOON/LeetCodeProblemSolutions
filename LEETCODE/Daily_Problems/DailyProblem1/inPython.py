class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ')':
                # Start to pop until finding a '('
                queue = []
                while stack and stack[-1] != '(':
                    queue.append(stack.pop())
                stack.pop()  # remove the '('
                # Add the reversed substring back to the stack
                stack.extend(queue)
            else:
                stack.append(char)
        # Join the final stack to form the result string
        return ''.join(stack)
