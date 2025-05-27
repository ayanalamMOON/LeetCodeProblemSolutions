class Solution:
	def survivedRobotsHealths(self, positions, healths, directions):
		n = len(positions)
		index = list(range(n))
		result = [-1] * n  # -1 means the robot is removed

		# Sort indices based on the positions
		index.sort(key=lambda x: positions[x])

		st = []  # Stack to store indices of robots moving right ('R')

		for i in index:
			if directions[i] == 'R':
				st.append(i)
			else:  # directions[i] == 'L'
				while st and healths[i] > 0:
					j = st[-1]
					if healths[j] > healths[i]:
						healths[j] -= 1
						healths[i] = 0
					elif healths[j] < healths[i]:
						st.pop()
						healths[i] -= 1
					else:
						st.pop()
						healths[j] = 0
						healths[i] = 0
				if healths[i] > 0:
					result[i] = healths[i]

		# Add remaining robots in the stack to the result
		while st:
			j = st.pop()
			result[j] = healths[j]

		# Collect the healths of surviving robots in the original order
		survivors = [result[i] for i in range(n) if result[i] != -1]

		return survivors