class Solution:
	def countOfAtoms(self, formula: str) -> str:
		def parse():
			N = len(formula)
			count = defaultdict(int)
			stack = deque()
			i = 0

			while i < N:
				if formula[i] == '(':
					stack.append(count)
					count = defaultdict(int)
					i += 1
				elif formula[i] == ')':
					i += 1
					# Extracting the multiplier if any
					i_start = i
					while i < N and formula[i].isdigit():
						i += 1
					multiplier = int(formula[i_start:i] or 1)

					# Merging counts with the top of the stack
					top_count = stack.pop()
					for element, cnt in count.items():
						top_count[element] += cnt * multiplier
					count = top_count
				else:
					# Parsing element name
					i_start = i
					i += 1
					while i < N and formula[i].islower():
						i += 1
					element = formula[i_start:i]

					# Parsing the count of the element
					i_start = i
					while i < N and formula[i].isdigit():
						i += 1
					count[element] += int(formula[i_start:i] or 1)

			return count

		# Parsing the formula
		element_count = parse()

		# Building and returning the result string
		return ''.join(f"{element}{(count if count > 1 else '')}" for element, count in sorted(element_count.items()))