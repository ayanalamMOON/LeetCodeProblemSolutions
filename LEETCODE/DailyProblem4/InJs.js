class Solution {
	countOfAtoms(formula) {
		let n = formula.length;
		let elementCount = new Map();
		let stack = []; // Stack to store counts and multipliers
		let i = 0;

		while (i < n) {
			if (formula[i] === '(') {
				stack.push([new Map(elementCount), 1]);
				elementCount.clear();
				i++;
			} else if (formula[i] === ')') {
				i++;
				let count = 0;
				while (i < n && !isNaN(formula[i])) {
					count = count * 10 + (formula.charCodeAt(i++) - '0'.charCodeAt(0));
				}
				if (count === 0) count = 1;

				if (stack.length > 0) {
					let [prevCount, multiplier] = stack.pop();
					for (let [elem, cnt] of elementCount) {
						prevCount.set(elem, (prevCount.get(elem) || 0) + cnt * count);
					}
					elementCount = prevCount;
				}
			} else {
				let start = i++;
				while (i < n && formula[i] >= 'a' && formula[i] <= 'z') ++i;
				let element = formula.substring(start, i);
				let count = 0;
				while (i < n && !isNaN(formula[i])) {
					count = count * 10 + (formula.charCodeAt(i++) - '0'.charCodeAt(0));
				}
				if (count === 0) count = 1;
				elementCount.set(element, (elementCount.get(element) || 0) + count);
			}
		}

		// Create result string
		let result = [...elementCount.entries()]
			.sort((a, b) => a[0].localeCompare(b[0]))
			.reduce((acc, [elem, cnt]) => acc + elem + (cnt > 1 ? cnt : ''), '');

		return result;
	}
}