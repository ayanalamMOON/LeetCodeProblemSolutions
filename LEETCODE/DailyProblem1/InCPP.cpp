class Solution {
public:
	string reverseParentheses(string s) {
		stack<char> stack;
		for (char& char : s) {
			if (char == ')') {
				// Start to pop until finding a '('
				queue<char> queue;
				while (!stack.empty() && stack.top() != '(') {
					queue.push(stack.top());
					stack.pop();
				}
				stack.pop();  // remove the '('
				// Add the reversed substring back to the stack
				while (!queue.empty()) {
					stack.push(queue.front());
					queue.pop();
				}
			} else {
				stack.push(char);
			}
		}
		// Join the final stack to form the result string
		string result;
		while (!stack.empty()) {
			result = stack.top() + result;
			stack.pop();
		}
		return result;
	}
};