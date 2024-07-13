#include <stdio.h>
#include <stdlib.h>
// A structure to represent a stack
struct Stack {
	int top;
	unsigned capacity;
	int* array;
};

// Function to create a stack of given capacity
struct Stack* createStack(unsigned capacity) {
	struct Stack* stack = (struct Stack*)malloc(sizeof(struct Stack));
	stack->capacity = capacity;
	stack->top = -1;
	stack->array = (int*)malloc(stack->capacity * sizeof(int));
	return stack;
}

// Stack is full when top is equal to the last index
int isFull(struct Stack* stack) {
	return stack->top == (int)stack->capacity - 1;
}

// Stack is empty when top is equal to -1
int isEmpty(struct Stack* stack) {
	return stack->top == -1;
}

// Function to add an item to stack. It increases top by 1
void push(struct Stack* stack, int item) {
	if (isFull(stack))
		return;
	stack->array[++stack->top] = item;
}

// Function to remove an item from stack. It decreases top by 1
int pop(struct Stack* stack) {
	if (isEmpty(stack))
		return -1;
	return stack->array[stack->top--];
}

// Function to get the top item from stack without removing it
int peek(struct Stack* stack) {
	if (isEmpty(stack))
		return -1;
	return stack->array[stack->top];
}

// Function to get index array sorted by positions
void sortIndicesByPositions(int* positions, int* index, int n) {
	for (int i = 0; i < n; ++i) {
		for (int j = i + 1; j < n; ++j) {
			if (positions[index[i]] > positions[index[j]]) {
				int temp = index[i];
				index[i] = index[j];
				index[j] = temp;
			}
		}
	}
}

// Main function to find survived robots' healths
void survivedRobotsHealths(int* positions, int* healths, char* directions, int n, int* result) {
	int* index = (int*)malloc(n * sizeof(int));
	for (int i = 0; i < n; ++i) {
		index[i] = i;
		result[i] = -1; // -1 means the robot is removed
	}

	sortIndicesByPositions(positions, index, n);

	struct Stack* st = createStack(n);

	for (int i = 0; i < n; ++i) {
		int idx = index[i];
		if (directions[idx] == 'R') {
			push(st, idx);
		} else { // directions[idx] == 'L'
			while (!isEmpty(st) && healths[idx] > 0) {
				int j = peek(st);
				if (healths[j] > healths[idx]) {
					healths[j]--;
					healths[idx] = 0;
				} else if (healths[j] < healths[idx]) {
					pop(st);
					healths[idx]--;
				} else {
					pop(st);
					healths[j] = 0;
					healths[idx] = 0;
				}
			}
			if (healths[idx] > 0) {
				result[idx] = healths[idx];
			}
		}
	}

	// Add remaining robots in the stack to the result
	while (!isEmpty(st)) {
		int j = pop(st);
		result[j] = healths[j];
	}

	free(index);
	free(st->array);
	free(st);
}