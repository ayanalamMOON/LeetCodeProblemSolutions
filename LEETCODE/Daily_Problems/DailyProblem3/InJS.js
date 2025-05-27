class Solution {
  survivedRobotsHealths(positions, healths, directions) {
	const n = positions.length;
	const index = Array.from({ length: n }, (_, i) => i);
	const result = new Array(n).fill(-1); // -1 means the robot is removed

	// Sort indices based on the positions
	index.sort((a, b) => positions[a] - positions[b]);

	const st = []; // Stack to store indices of robots moving right ('R')

	for (const i of index) {
	  if (directions[i] === 'R') {
		st.push(i);
	  } else { // directions[i] === 'L'
		while (st.length && healths[i] > 0) {
		  const j = st[st.length - 1];
		  if (healths[j] > healths[i]) {
			healths[j] -= 1;
			healths[i] = 0;
		  } else if (healths[j] < healths[i]) {
			st.pop();
			healths[i] -= 1;
		  } else {
			st.pop();
			healths[j] = 0;
			healths[i] = 0;
		  }
		}
		if (healths[i] > 0) {
		  result[i] = healths[i];
		}
	  }
	}

	// Add remaining robots in the stack to the result
	while (st.length) {
	  const j = st.pop();
	  result[j] = healths[j];
	}

	// Collect the healths of surviving robots in the original order
	const survivors = result.filter(r => r !== -1);

	return survivors;
  }
}