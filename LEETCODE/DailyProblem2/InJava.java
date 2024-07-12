public class Solution {
	public int maximumGain(String s, int x, int y) {
		int totalPoints = 0;

		if (x < y) {
			// Swap to always prioritize the higher points first
			int temp = x;
			x = y;
			y = temp;
			s = s.replace('a', 'temp').replace('b', 'a').replace('temp', 'b');
		}

		// Function to remove a specific pattern and count points
		java.util.function.BiFunction<Character, Character, Integer> removePattern = (first, second) -> {
			StringBuilder newString = new StringBuilder();
			int points = 0;
			for (char c : s.toCharArray()) {
				if (newString.length() > 0 && newString.charAt(newString.length() - 1) == first && c == second) {
					newString.deleteCharAt(newString.length() - 1);
					points += (first == 'a' && second == 'b') ? x : y;
				} else {
					newString.append(c);
				}
			}
			s = newString.toString();
			return points;
		};

		// First remove "ab" to get x points (if x >= y)
		totalPoints += removePattern.apply('a', 'b');

		// Then remove "ba" to get y points
		totalPoints += removePattern.apply('b', 'a');

		return totalPoints;
	}
}