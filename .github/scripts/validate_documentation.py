#!/usr/bin/env python3
"""
Documentation Structure Validator
=================================

Validates the structure and consistency of all documentation files.
"""

import os
import re
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DocumentationValidator:
    def __init__(self):
        self.root_path = Path(".")
        self.errors = []
        self.warnings = []
    
    def validate_readme(self) -> None:
        """Validate README.md structure"""
        readme_path = self.root_path / "README.md"
        if not readme_path.exists():
            self.errors.append("README.md not found")
            return
        
        content = readme_path.read_text(encoding='utf-8')
        
        # Check for required sections
        required_sections = [
            "# LeetCode Problem Solutions",
            "## Repository Structure", 
            "## Daily Problems",
            "## Language Support"
        ]
        
        for section in required_sections:
            if section not in content:
                self.warnings.append(f"README.md missing section: {section}")
        
        logger.info("README.md validation completed")
    
    def validate_index(self) -> None:
        """Validate INDEX.md structure"""
        index_path = self.root_path / "INDEX.md"
        if not index_path.exists():
            self.errors.append("INDEX.md not found")
            return
        
        content = index_path.read_text(encoding='utf-8')
        
        # Check for required sections
        required_sections = [
            "# Problem Index",
            "## By Difficulty",
            "## By Topic"
        ]
        
        for section in required_sections:
            if section not in content:
                self.warnings.append(f"INDEX.md missing section: {section}")
        
        logger.info("INDEX.md validation completed")
    
    def validate_performance_analysis(self) -> None:
        """Validate PERFORMANCE_ANALYSIS.md structure"""
        perf_path = self.root_path / "PERFORMANCE_ANALYSIS.md"
        if not perf_path.exists():
            self.errors.append("PERFORMANCE_ANALYSIS.md not found")
            return
        
        logger.info("PERFORMANCE_ANALYSIS.md validation completed")
    
    def validate_interview_prep(self) -> None:
        """Validate InterviewPreparation.md structure"""
        interview_path = self.root_path / "InterviewPreparation.md"
        if not interview_path.exists():
            self.errors.append("InterviewPreparation.md not found")
            return
        
        logger.info("InterviewPreparation.md validation completed")
    
    def run(self) -> int:
        """Run all validations"""
        logger.info("Starting documentation validation...")
        
        self.validate_readme()
        self.validate_index()
        self.validate_performance_analysis()
        self.validate_interview_prep()
        
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
            logger.info("✅ All documentation validation checks passed!")
        
        return len(self.errors)

if __name__ == "__main__":
    validator = DocumentationValidator()
    exit_code = validator.run()
    exit(exit_code)
