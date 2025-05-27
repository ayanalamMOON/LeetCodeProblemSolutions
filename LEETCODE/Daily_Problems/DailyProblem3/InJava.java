public class Solution {
    public List<Integer> survivedRobotsHealths(int[] positions, int[] healths, String directions) {
        int n = positions.length;
        Integer[] index = new Integer[n];
        Integer[] result = new Integer[n];
        Arrays.fill(result, -1); // -1 means the robot is removed

        // Initialize index with 0 to n-1
        for (int i = 0; i < n; ++i) {
            index[i] = i;
        }

        // Sort indices based on the positions
        Arrays.sort(index, (a, b) -> Integer.compare(positions[a], positions[b]));

        Stack<Integer> st = new Stack<>(); // Stack to store indices of robots moving right ('R')

        for (int i : index) {
            if (directions.charAt(i) == 'R') {
                st.push(i);
            } else { // directions[i] == 'L'
                while (!st.isEmpty() && healths[i] > 0) {
                    int j = st.peek();
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
        while (!st.isEmpty()) {
            int j = st.pop();
            result[j] = healths[j];
        }

        // Collect the healths of surviving robots in the original order
        List<Integer> survivors = new ArrayList<>();
        for (int i = 0; i < n; ++i) {
            if (result[i] != -1) {
                survivors.add(result[i]);
            }
        }

        return survivors;
    }
}