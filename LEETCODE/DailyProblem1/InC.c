
// Define a stack structure
typedef struct {
    char* data;
    int top;
    int capacity;
} Stack;

// Function to initialize the stack
void initStack(Stack* stack, int capacity) {
    stack->data = (char*)malloc(capacity * sizeof(char));
    stack->top = -1;
    stack->capacity = capacity;
}

// Function to check if the stack is empty
int isEmpty(Stack* stack) {
    return stack->top == -1;
}

// Function to push an element to the stack
void push(Stack* stack, char element) {
    if (stack->top == stack->capacity - 1) {
        // Resize the stack if it's full
        stack->capacity *= 2;
        stack->data = (char*)realloc(stack->data, stack->capacity * sizeof(char));
    }
    stack->data[++stack->top] = element;
}

// Function to pop an element from the stack
char pop(Stack* stack) {
    if (!isEmpty(stack)) {
        return stack->data[stack->top--];
    }
    return '\0'; // Return null character if stack is empty
}

// Function to reverse the substring between parentheses
char* reverseParentheses(char* s) {
    int length = strlen(s);
    Stack stack;
    initStack(&stack, length);

    for (int i = 0; i < length; i++) {
        if (s[i] == ')') {
            // Temporary stack to hold characters to be reversed
            Stack tempStack;
            initStack(&tempStack, length);
            while (!isEmpty(&stack) && stack.data[stack.top] != '(') {
                push(&tempStack, pop(&stack));
            }
            pop(&stack); // Remove the '('

            // Push the reversed characters back to the main stack
            while (!isEmpty(&tempStack)) {
                push(&stack, pop(&tempStack));
            }
            free(tempStack.data); // Free the temporary stack
        } else {
            push(&stack, s[i]);
        }
    }

    // Construct the result string
    char* result = (char*)malloc((stack.top + 2) * sizeof(char)); // +1 for null terminator
    for (int i = stack.top; i >= 0; i--) {
        result[stack.top - i] = stack.data[i];
    }
    result[stack.top + 1] = '\0'; // Null-terminate the string

    free(stack.data); // Free the stack
    return result;
}

