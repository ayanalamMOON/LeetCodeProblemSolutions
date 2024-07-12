class Solution:
	def maximumGain(self, s: str, x: int, y: int) -> int:
		totalPoints = 0

		if x < y:
			# Swap to always prioritize the higher points first
			x, y = y, x
			s = s.replace('a', 'temp').replace('b', 'a').replace('temp', 'b')

		def removePattern(s: str, first: str, second: str, points: int) -> str:
			newString = []
			totalPoints = 0
			for c in s:
				if newString and newString[-1] == first and c == second:
					newString.pop()
					totalPoints += points
				else:
					newString.append(c)
			return ''.join(newString), totalPoints

		# First remove "ab" to get x points (if x >= y)
		s, points = removePattern(s, 'a', 'b', x)
		totalPoints += points

		# Then remove "ba" to get y points
		s, points = removePattern(s, 'b', 'a', y)
		totalPoints += points

		return totalPoints