class Solution {
public:
    int maximumGain(string s, int x, int y) {
        int totalPoints = 0;

        if (x < y) {
            // Swap to always prioritize the higher points first
            swap(x, y);
            swap(s, s);
            for (char &c : s) {
                if (c == 'a') c = 'b';
                else if (c == 'b') c = 'a';
            }
        }

        // Function to remove a specific pattern and count points
        auto removePattern = [&](char first, char second, int points) {
            string newString;
            for (char c : s) {
                if (!newString.empty() && newString.back() == first && c == second) {
                    newString.pop_back();
                    totalPoints += points;
                } else {
                    newString.push_back(c);
                }
            }
            s = newString;
        };

        // First remove "ab" to get x points (if x >= y)
        removePattern('a', 'b', x);

        // Then remove "ba" to get y points
        removePattern('b', 'a', y);

        return totalPoints;
    }
};
