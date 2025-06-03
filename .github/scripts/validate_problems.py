#!/usr/bin/env python3
"""
Problem Structure Validator
===========================

Validates that all problem directories have the required structure.
"""

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ProblemValidator:
    def __init__(self):
        self.root_path = Path(".")
        self.errors = []
        self.warnings = []
    
    def validate_problem_directory(self, problem_dir: Path) -> None:
        """Validate a single problem directory"""
        logger.info(f"Validating {problem_dir.name}...")
        
        # Check for Problem.md
        if not (problem_dir / "Problem.md").exists():
            self.errors.append(f"{problem_dir.name}: Missing Problem.md")
        
        # Check for at least one solution file
        solution_files = [
            "InCPP.cpp", "InC++.cpp", "inC++.cpp",
            "InJava.java",
            "InPython.py", "inPython.py", 
            "InJS.js", "InJs.js",
            "InRust.rs",
            "InC.c"
        ]
        
        has_solution = False
        for solution_file in solution_files:
            if (problem_dir / solution_file).exists():
                has_solution = True
                break
        
        if not has_solution:
            self.warnings.append(f"{problem_dir.name}: No solution files found")
        
        # Check Problem.md structure
        problem_md = problem_dir / "Problem.md"
        if problem_md.exists():
            content = problem_md.read_text(encoding='utf-8')
            
            # Check for required sections
            required_patterns = [
                r'#\s*\d+\.',  # Problem number and title
                r'\*\*Difficulty\*\*:',  # Difficulty
            ]
            
            for pattern in required_patterns:
                if not re.search(pattern, content):
                    self.warnings.append(f"{problem_dir.name}: Problem.md missing required pattern: {pattern}")
    
    def run(self) -> int:
        """Validate all problem directories"""
        logger.info("Starting problem structure validation...")
        
        # Validate Daily Problems
        daily_dir = self.root_path / "Daily_Problems"
        if daily_dir.exists():
            for problem_dir in daily_dir.iterdir():
                if problem_dir.is_dir() and problem_dir.name.startswith("DailyProblem"):
                    self.validate_problem_directory(problem_dir)
        
        # Validate Regular Problems
        for dir_name in ["Regular_Practice_Problems", "Rgegular_Practice_Problems"]:
            regular_dir = self.root_path / dir_name
            if regular_dir.exists():
                for problem_dir in regular_dir.iterdir():
                    if problem_dir.is_dir() and problem_dir.name.startswith("Problem"):
                        self.validate_problem_directory(problem_dir)
        
        # Report results
        if self.errors:
            logger.error(f"Found {len(self.errors)} errors:")
            for error in self.errors:
                logger.error(f"  ❌ {error}")
        
        if self.warnings:
            logger.warning(f"Found {len(self.warnings)} warnings:")
            for warning in self.warnings:
                logger.warning(f"  ⚠️  {warning}")
        
        if not self.errors and not self.warnings:
            logger.info("✅ All problem structures are valid!")
        
        return len(self.errors)

if __name__ == "__main__":
    import re
    validator = ProblemValidator()
    exit_code = validator.run()
    exit(exit_code)
