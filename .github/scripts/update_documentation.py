#!/usr/bin/env python3
"""
LeetCode Problem Solutions - Documentation Auto-Updater
=========================================================

This script automatically updates all documentation files when new problems
are added to the repository. It scans for new problem directories and updates:
- README.md
- INDEX.md  
- PERFORMANCE_ANALYSIS.md
- InterviewPreparation.md

Author: GitHub Actions Bot
Date: June 2025
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DocumentationUpdater:
    def __init__(self):
        self.root_path = Path(".")
        self.problems_data = {}
        self.daily_problems = []
        self.regular_problems = []
        
    def scan_problems(self) -> None:
        """Scan all problem directories and extract metadata"""
        logger.info("Scanning problem directories...")
        
        # Scan Daily Problems
        daily_dir = self.root_path / "Daily_Problems"
        if daily_dir.exists():
            for problem_dir in daily_dir.iterdir():
                if problem_dir.is_dir() and problem_dir.name.startswith("DailyProblem"):
                    problem_data = self._extract_problem_data(problem_dir, "daily")
                    if problem_data:
                        self.daily_problems.append(problem_data)
        
        # Scan Regular Problems (handle both spellings)
        for dir_name in ["Regular_Practice_Problems", "Rgegular_Practice_Problems"]:
            regular_dir = self.root_path / dir_name
            if regular_dir.exists():
                for problem_dir in regular_dir.iterdir():
                    if problem_dir.is_dir() and problem_dir.name.startswith("Problem"):
                        problem_data = self._extract_problem_data(problem_dir, "regular")
                        if problem_data:
                            self.regular_problems.append(problem_data)
        
        logger.info(f"Found {len(self.daily_problems)} daily problems and {len(self.regular_problems)} regular problems")
    
    def _extract_problem_data(self, problem_dir: Path, problem_type: str) -> Optional[Dict]:
        """Extract metadata from a problem directory"""
        try:
            problem_md = problem_dir / "Problem.md"
            if not problem_md.exists():
                logger.warning(f"No Problem.md found in {problem_dir}")
                return None
            
            content = problem_md.read_text(encoding='utf-8')
            
            # Extract problem number and title
            title_match = re.search(r'#\s*(\d+)\.\s*(.+)', content)
            if not title_match:
                logger.warning(f"Could not extract title from {problem_md}")
                return None
            
            problem_num = title_match.group(1)
            problem_title = title_match.group(2).strip()
            
            # Extract difficulty
            difficulty_match = re.search(r'\*\*Difficulty\*\*:\s*(\w+)', content)
            difficulty = difficulty_match.group(1) if difficulty_match else "Unknown"
            
            # Extract topic/tags
            topics = []
            topic_match = re.search(r'\*\*Topics?\*\*:\s*(.+)', content)
            if topic_match:
                topics = [t.strip() for t in topic_match.group(1).split(',')]
            
            # Check available languages
            languages = []
            language_files = {
                'C++': ['InCPP.cpp', 'InC++.cpp', 'inC++.cpp'],
                'Java': ['InJava.java'],
                'Python': ['InPython.py', 'inPython.py'],
                'JavaScript': ['InJS.js', 'InJs.js'],
                'Rust': ['InRust.rs'],
                'C': ['InC.c']
            }
            
            for lang, possible_files in language_files.items():
                for file_name in possible_files:
                    if (problem_dir / file_name).exists():
                        languages.append(lang)
                        break
            
            return {
                'number': problem_num,
                'title': problem_title,
                'difficulty': difficulty,
                'topics': topics,
                'languages': languages,
                'directory': str(problem_dir.relative_to(self.root_path)),
                'type': problem_type,
                'folder_name': problem_dir.name
            }
            
        except Exception as e:
            logger.error(f"Error processing {problem_dir}: {e}")
            return None
    
    def update_readme(self) -> None:
        """Update README.md with new problems"""
        logger.info("Updating README.md...")
        
        readme_path = self.root_path / "README.md"
        if not readme_path.exists():
            logger.error("README.md not found")
            return
        
        content = readme_path.read_text(encoding='utf-8')
        
        # Update repository structure
        content = self._update_readme_structure(content)
        
        # Update daily problems table
        content = self._update_daily_problems_table(content)
        
        # Update statistics
        content = self._update_readme_statistics(content)
        
        readme_path.write_text(content, encoding='utf-8')
        logger.info("README.md updated successfully")
    
    def _update_readme_structure(self, content: str) -> str:
        """Update the repository structure section"""
        # Find the structure section
        structure_start = content.find("```")
        if structure_start == -1:
            return content
        
        structure_end = content.find("```", structure_start + 3)
        if structure_end == -1:
            return content
        
        # Generate new structure
        structure_lines = [
            "# Code Citations.md",
            "CONTRIBUTING.md",
            "INDEX.md", 
            "InterviewPreparation.md",
            "LANGUAGE_GUIDE.md",
            "PERFORMANCE_ANALYSIS.md",
            "README.md",
            "Daily_Problems/"
        ]
        
        # Add daily problems
        for problem in sorted(self.daily_problems, key=lambda x: int(x['number'])):
            structure_lines.append(f"\t{problem['folder_name']}/")
            structure_lines.append(f"\t\tProblem.md")
            if "C++" in problem['languages']:
                structure_lines.append(f"\t\tInCPP.cpp")
            if "C" in problem['languages']:
                structure_lines.append(f"\t\tInC.c")
            if "Java" in problem['languages']:
                structure_lines.append(f"\t\tInJava.java")
            if "Python" in problem['languages']:
                structure_lines.append(f"\t\tInPython.py")
            if "JavaScript" in problem['languages']:
                structure_lines.append(f"\t\tInJS.js")
            if "Rust" in problem['languages']:
                structure_lines.append(f"\t\tInRust.rs")
            if len(problem['languages']) > 3:  # Add Procedure.md for complex problems
                structure_lines.append(f"\t\tProcedure.md")
        
        # Add regular problems if they exist
        if self.regular_problems:
            structure_lines.append("Regular_Practice_Problems/")
            for problem in sorted(self.regular_problems, key=lambda x: int(x['number'])):
                structure_lines.append(f"\t{problem['folder_name']}/")
                structure_lines.append(f"\t\tProblem.md")
        
        new_structure = "\n".join(structure_lines)
        
        return content[:structure_start + 3] + "\n" + new_structure + "\n" + content[structure_end:]
    
    def _update_daily_problems_table(self, content: str) -> str:
        """Update the daily problems table"""
        # Find the daily problems table
        table_pattern = r"(\| Problem \| Difficulty \| Languages \| Status \|\n\|[^\n]+\|\n)(.*?)(\n\n|\n(?=[^|]))"
        
        def create_table_rows():
            rows = []
            for problem in sorted(self.daily_problems, key=lambda x: int(x['number'])):
                lang_badges = []
                for lang in problem['languages']:
                    lang_badges.append(f"![{lang}](https://img.shields.io/badge/{lang.replace('+', '%2B')}-00599C?style=flat-square)")
                
                languages_str = " ".join(lang_badges)
                status = "✅ Complete" if len(problem['languages']) >= 3 else "🔄 In Progress"
                
                rows.append(f"| [{problem['number']}. {problem['title']}]({problem['directory']}/Problem.md) | {problem['difficulty']} | {languages_str} | {status} |")
            
            return "\n".join(rows)
        
        table_rows = create_table_rows()
        
        def replacement_func(match):
            return match.group(1) + table_rows + match.group(3)
        
        return re.sub(table_pattern, replacement_func, content, flags=re.DOTALL)
    
    def _update_readme_statistics(self, content: str) -> str:
        """Update repository statistics"""
        total_problems = len(self.daily_problems) + len(self.regular_problems)
        total_solutions = sum(len(p['languages']) for p in self.daily_problems + self.regular_problems)
        
        # Update stats in badges or stats section
        content = re.sub(r'(\d+)\s*Problems', f'{total_problems} Problems', content)
        content = re.sub(r'(\d+)\s*Solutions', f'{total_solutions} Solutions', content)
        
        return content
    
    def update_index(self) -> None:
        """Update INDEX.md with new problems"""
        logger.info("Updating INDEX.md...")
        
        index_path = self.root_path / "INDEX.md"
        if not index_path.exists():
            logger.error("INDEX.md not found")
            return
        
        content = index_path.read_text(encoding='utf-8')
        
        # Update various sections
        content = self._update_index_problems_list(content)
        content = self._update_index_by_difficulty(content)
        content = self._update_index_by_topic(content)
        content = self._update_implementation_matrix(content)
        
        index_path.write_text(content, encoding='utf-8')
        logger.info("INDEX.md updated successfully")
    
    def _update_index_problems_list(self, content: str) -> str:
        """Update the main problems list in INDEX"""
        # This would contain logic to update the problems list
        # Implementation details would depend on your INDEX.md structure
        return content
    
    def _update_index_by_difficulty(self, content: str) -> str:
        """Update problems organized by difficulty"""
        return content
    
    def _update_index_by_topic(self, content: str) -> str:
        """Update problems organized by topic"""
        return content
    
    def _update_implementation_matrix(self, content: str) -> str:
        """Update the implementation status matrix"""
        return content
    
    def update_performance_analysis(self) -> None:
        """Update PERFORMANCE_ANALYSIS.md with new problems"""
        logger.info("Updating PERFORMANCE_ANALYSIS.md...")
        
        perf_path = self.root_path / "PERFORMANCE_ANALYSIS.md"
        if not perf_path.exists():
            logger.error("PERFORMANCE_ANALYSIS.md not found")
            return
        
        content = perf_path.read_text(encoding='utf-8')
        
        # Add performance entries for new problems
        for problem in self.daily_problems + self.regular_problems:
            if not self._problem_exists_in_performance(content, problem['number']):
                content = self._add_performance_entry(content, problem)
        
        perf_path.write_text(content, encoding='utf-8')
        logger.info("PERFORMANCE_ANALYSIS.md updated successfully")
    
    def _problem_exists_in_performance(self, content: str, problem_num: str) -> bool:
        """Check if problem already exists in performance analysis"""
        return f"Problem {problem_num}" in content
    
    def _add_performance_entry(self, content: str, problem: Dict) -> str:
        """Add a performance entry for a new problem"""
        # Add basic performance template
        performance_template = f"""
### Problem {problem['number']}: {problem['title']}

| Language | Time Complexity | Space Complexity | Runtime | Memory |
|----------|----------------|------------------|---------|--------|
| C++ | O(n) | O(1) | TBD ms | TBD MB |
| Java | O(n) | O(1) | TBD ms | TBD MB |
| Python | O(n) | O(1) | TBD ms | TBD MB |
| JavaScript | O(n) | O(1) | TBD ms | TBD MB |
| Rust | O(n) | O(1) | TBD ms | TBD MB |

**Analysis**: Performance analysis pending - please run benchmarks and update.

"""
        
        # Append to end of file
        return content + performance_template
    
    def update_interview_preparation(self) -> None:
        """Update InterviewPreparation.md with new problems"""
        logger.info("Updating InterviewPreparation.md...")
        
        interview_path = self.root_path / "InterviewPreparation.md"
        if not interview_path.exists():
            logger.error("InterviewPreparation.md not found")
            return
        
        content = interview_path.read_text(encoding='utf-8')
        
        # Add references to new problems in appropriate sections based on topics
        for problem in self.daily_problems + self.regular_problems:
            content = self._add_interview_references(content, problem)
        
        interview_path.write_text(content, encoding='utf-8')
        logger.info("InterviewPreparation.md updated successfully")
    
    def _add_interview_references(self, content: str, problem: Dict) -> str:
        """Add problem references to appropriate interview prep sections"""
        # This would add problems to relevant sections based on their topics
        # For now, return content unchanged to avoid breaking existing structure
        return content
    
    def run(self) -> None:
        """Main execution method"""
        logger.info("Starting documentation update process...")
        
        self.scan_problems()
        
        if not self.daily_problems and not self.regular_problems:
            logger.info("No problems found to process")
            return
        
        self.update_readme()
        self.update_index()
        self.update_performance_analysis()
        self.update_interview_preparation()
        
        logger.info("Documentation update completed successfully!")

if __name__ == "__main__":
    updater = DocumentationUpdater()
    updater.run()
