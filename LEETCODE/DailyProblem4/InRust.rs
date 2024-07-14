use std::collections::{HashMap, VecDeque};

struct Solution;

impl Solution {
	pub fn count_of_atoms(formula: String) -> String {
		let mut element_count: HashMap<String, i32> = HashMap::new();
		let mut stack: VecDeque<HashMap<String, i32>> = VecDeque::new();
		let chars: Vec<char> = formula.chars().collect();
		let mut i = 0;
		let n = chars.len();

		while i < n {
			match chars[i] {
				'(' => {
					stack.push_back(element_count.clone());
					element_count.clear();
					i += 1;
				}
				')' => {
					i += 1;
					let mut count = 0;
					while i < n && chars[i].is_digit(10) {
						count = count * 10 + chars[i].to_digit(10).unwrap() as i32;
						i += 1;
					}
					if count == 0 {
						count = 1;
					}
					if let Some(prev_count) = stack.pop_back() {
						for (elem, cnt) in element_count.iter() {
							*prev_count.entry(elem.clone()).or_insert(0) += cnt * count;
						}
						element_count = prev_count;
					}
				}
				_ => {
					let start = i;
					i += 1;
					while i < n && chars[i].is_lowercase() {
						i += 1;
					}
					let element: String = chars[start..i].iter().collect();
					let mut count = 0;
					while i < n && chars[i].is_digit(10) {
						count = count * 10 + chars[i].to_digit(10).unwrap() as i32;
						i += 1;
					}
					if count == 0 {
						count = 1;
					}
					*element_count.entry(element).or_insert(0) += count;
				}
			}
		}

		let mut elements: Vec<_> = element_count.iter().collect();
		elements.sort_by(|a, b| a.0.cmp(b.0));
		let mut result = String::new();
		for (elem, &cnt) in elements {
			result.push_str(elem);
			if cnt > 1 {
				result.push_str(&cnt.to_string());
			}
		}

		result
	}
}