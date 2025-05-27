class Solution {
public:
    string countOfAtoms(string formula) {
        int n = formula.size();
        map<string, int> elementCount;
        stack<pair<map<string, int>, int>> st; // stack to store counts and multipliers
        int i = 0;

        while (i < n) {
            if (formula[i] == '(') {
                st.push({elementCount, 1});
                elementCount.clear();
                i++;
            } else if (formula[i] == ')') {
                i++;
                int count = 0;
                while (i < n && isdigit(formula[i])) {
                    count = count * 10 + (formula[i++] - '0');
                }
                if (count == 0) count = 1;

                if (!st.empty()) {
                    auto [prevCount, multiplier] = st.top();
                    st.pop();
                    for (auto& [elem, cnt] : elementCount) {
                        prevCount[elem] += cnt * count;
                    }
                    elementCount = prevCount;
                }
            } else {
                int start = i++;
                while (i < n && islower(formula[i])) ++i;
                string element = formula.substr(start, i - start);
                int count = 0;
                while (i < n && isdigit(formula[i])) {
                    count = count * 10 + (formula[i++] - '0');
                }
                if (count == 0) count = 1;
                elementCount[element] += count;
            }
        }

        // Create result string
        stringstream result;
        for (const auto& [elem, cnt] : elementCount) {
            result << elem;
            if (cnt > 1) result << cnt;
        }

        return result.str();
    }
};