public class Solution {
	public String countOfAtoms(String formula) {
		int n = formula.length();
		TreeMap<String, Integer> elementCount = new TreeMap<>();
		Stack<Map.Entry<TreeMap<String, Integer>, Integer>> stack = new Stack<>();
		int i = 0;

		while (i < n) {
			if (formula.charAt(i) == '(') {
				stack.push(new AbstractMap.SimpleEntry<>(new TreeMap<>(elementCount), 1));
				elementCount.clear();
				i++;
			} else if (formula.charAt(i) == ')') {
				i++;
				int count = 0;
				while (i < n && Character.isDigit(formula.charAt(i))) {
					count = count * 10 + (formula.charAt(i++) - '0');
				}
				if (count == 0) count = 1;

				if (!stack.isEmpty()) {
					Map.Entry<TreeMap<String, Integer>, Integer> entry = stack.pop();
					TreeMap<String, Integer> prevCount = entry.getKey();
					for (Map.Entry<String, Integer> e : elementCount.entrySet()) {
						prevCount.merge(e.getKey(), e.getValue() * count, Integer::sum);
					}
					elementCount = prevCount;
				}
			} else {
				int start = i++;
				while (i < n && Character.isLowerCase(formula.charAt(i))) ++i;
				String element = formula.substring(start, i);
				int count = 0;
				while (i < n && Character.isDigit(formula.charAt(i))) {
					count = count * 10 + (formula.charAt(i++) - '0');
				}
				if (count == 0) count = 1;
				elementCount.merge(element, count, Integer::sum);
			}
		}

		// Create result string
		StringBuilder result = new StringBuilder();
		for (Map.Entry<String, Integer> entry : elementCount.entrySet()) {
			result.append(entry.getKey());
			if (entry.getValue() > 1) result.append(entry.getValue());
		}

		return result.toString();
	}
}