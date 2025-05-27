struct Solution;

impl Solution {
    pub fn maximum_gain(s: String, x: i32, y: i32) -> i32 {
        let (mut x, mut y, mut s) = if x < y {
            // Swap to always prioritize the higher points first
            let swapped_s: String = s.chars().map(|c| if c == 'a' { 'b' } else if c == 'b' { 'a' } else { c }).collect();
            (y, x, swapped_s)
        } else {
            (x, y, s)
        };

        let mut total_points = 0;

        // Function to remove a specific pattern and count points
        let mut remove_pattern = |first: char, second: char, points: i32, s: &mut String| {
            let mut new_string = String::new();
            let mut chars = s.chars().collect::<Vec<char>>();
            let mut i = 0;
            while i < chars.len() {
                if i + 1 < chars.len() && chars[i] == first && chars[i + 1] == second {
                    total_points += points;
                    i += 2; // Skip the next character as well
                } else {
                    new_string.push(chars[i]);
                    i += 1;
                }
            }
            *s = new_string;
        };

        // First remove "ab" to get x points (if x >= y)
        remove_pattern('a', 'b', x, &mut s);

        // Then remove "ba" to get y points
        remove_pattern('b', 'a', y, &mut s);

        total_points
    }
}

fn main() {
    let s = "cdbcbbaaabab".to_string();
    let x = 4;
    let y = 5;
    let result = Solution::maximum_gain(s, x, y);
    println!("{}", result); // Expected output: the maximum points you can gain
}