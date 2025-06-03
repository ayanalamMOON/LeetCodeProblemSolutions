#!/usr/bin/env python3
"""
Manual Documentation Update Script
=================================

Allows manual triggering of documentation updates with specific options.
"""

import argparse
import sys
from pathlib import Path

# Import the main updater
sys.path.append(str(Path(__file__).parent))
from update_documentation import DocumentationUpdater

class ManualUpdater(DocumentationUpdater):
    def __init__(self, update_type: str, force: bool):
        super().__init__()
        self.update_type = update_type
        self.force = force
    
    def run(self) -> None:
        """Run manual update based on specified type"""
        print(f"Starting manual documentation update (type: {self.update_type}, force: {self.force})")
        
        self.scan_problems()
        
        if not self.force and not self.daily_problems and not self.regular_problems:
            print("No problems found and force=False, skipping update")
            return
        
        if self.update_type in ['all', 'readme']:
            print("Updating README.md...")
            self.update_readme()
        
        if self.update_type in ['all', 'index']:
            print("Updating INDEX.md...")
            self.update_index()
        
        if self.update_type in ['all', 'performance']:
            print("Updating PERFORMANCE_ANALYSIS.md...")
            self.update_performance_analysis()
        
        if self.update_type in ['all', 'interview-prep']:
            print("Updating InterviewPreparation.md...")
            self.update_interview_preparation()
        
        print("Manual documentation update completed!")

def main():
    parser = argparse.ArgumentParser(description='Manual documentation updater')
    parser.add_argument('--type', choices=['all', 'readme', 'index', 'performance', 'interview-prep'], 
                       default='all', help='Type of update to perform')
    parser.add_argument('--force', type=bool, default=False, 
                       help='Force update even if no changes detected')
    
    args = parser.parse_args()
    
    updater = ManualUpdater(args.type, args.force)
    updater.run()

if __name__ == "__main__":
    main()
