#!/usr/bin/env python3
"""
Link Checker for Documentation
==============================

Checks for broken internal links in all markdown files.
"""

import os
import re
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LinkChecker:
    def __init__(self):
        self.root_path = Path(".")
        self.broken_links = []
    
    def check_file_links(self, file_path: Path) -> None:
        """Check all links in a markdown file"""
        if not file_path.exists():
            return
        
        content = file_path.read_text(encoding='utf-8')
        
        # Find all markdown links [text](url)
        link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        links = re.findall(link_pattern, content)
        
        for link_text, link_url in links:
            # Skip external links (http/https)
            if link_url.startswith(('http://', 'https://', 'mailto:')):
                continue
            
            # Skip anchors
            if link_url.startswith('#'):
                continue
            
            # Check if file exists
            target_path = file_path.parent / link_url
            if not target_path.exists():
                # Try relative to root
                target_path = self.root_path / link_url
                if not target_path.exists():
                    self.broken_links.append({
                        'file': str(file_path),
                        'link_text': link_text,
                        'link_url': link_url
                    })
    
    def run(self) -> int:
        """Check all markdown files for broken links"""
        logger.info("Starting link validation...")
        
        # Check all markdown files
        md_files = list(self.root_path.glob("*.md"))
        md_files.extend(self.root_path.glob("**/*.md"))
        
        for md_file in md_files:
            # Skip files in .git directory
            if '.git' in str(md_file):
                continue
            self.check_file_links(md_file)
        
        # Report results
        if self.broken_links:
            logger.error(f"Found {len(self.broken_links)} broken links:")
            for link in self.broken_links:
                logger.error(f"  ❌ {link['file']}: [{link['link_text']}]({link['link_url']})")
        else:
            logger.info("✅ All links are valid!")
        
        return len(self.broken_links)

if __name__ == "__main__":
    checker = LinkChecker()
    exit_code = checker.run()
    exit(exit_code)
