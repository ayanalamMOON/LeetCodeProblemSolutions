use std::collections::VecDeque;

struct Solution;

impl Solution {
    pub fn survived_robots_healths(positions: Vec<i32>, mut healths: Vec<i32>, directions: String) -> Vec<i32> {
        let n = positions.len();
        let mut index: Vec<usize> = (0..n).collect();
        let mut result: Vec<i32> = vec![-1; n]; // -1 means the robot is removed

        // Sort indices based on the positions
        index.sort_unstable_by_key(|&i| positions[i]);

        let mut st: VecDeque<usize> = VecDeque::new(); // Stack to store indices of robots moving right ('R')

        for &i in &index {
            match directions.chars().nth(i).unwrap() {
                'R' => st.push_back(i),
                'L' => {
                    while let Some(&j) = st.back() {
                        if healths[j] > healths[i] {
                            healths[j] -= 1;
                            healths[i] = 0;
                            break;
                        } else if healths[j] < healths[i] {
                            st.pop_back();
                            healths[i] -= 1;
                        } else {
                            st.pop_back();
                            healths[j] = 0;
                            healths[i] = 0;
                            break;
                        }
                    }
                    if healths[i] > 0 {
                        result[i] = healths[i];
                    }
                }
                _ => {}
            }
        }

        // Add remaining robots in the stack to the result
        while let Some(j) = st.pop_back() {
            result[j] = healths[j];
        }

        // Collect the healths of surviving robots in the original order
        result.into_iter().filter(|&r| r != -1).collect()
    }
}