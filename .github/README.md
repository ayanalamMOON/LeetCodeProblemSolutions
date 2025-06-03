# 🚀 CI/CD Pipeline Documentation

This directory contains the automated CI/CD pipeline for the LeetCode Problem Solutions repository. The pipeline automatically updates all documentation files when new problems are added.

## 📁 Structure

```
.github/
├── workflows/
│   ├── auto-update-docs.yml    # Main auto-update workflow
│   ├── validate-docs.yml       # Documentation validation
│   └── manual-update.yml       # Manual update trigger
└── scripts/
    ├── update_documentation.py # Main documentation updater
    ├── validate_documentation.py # Documentation validator
    ├── check_links.py          # Link checker
    ├── validate_problems.py    # Problem structure validator
    └── manual_update.py        # Manual update script
```

## 🔄 Workflows

### 1. Auto-Update Documentation (`auto-update-docs.yml`)

**Triggers:**
- Push to `main`/`master` branch with changes in problem directories
- Pull requests affecting problem directories

**Actions:**
- Detects new/modified problems
- Scans problem metadata (title, difficulty, topics, languages)
- Updates all documentation files:
  - `README.md` - Repository structure and problem tables
  - `INDEX.md` - Problem indices and categorization
  - `PERFORMANCE_ANALYSIS.md` - Performance metrics and analysis
  - `InterviewPreparation.md` - Interview references and examples
- Commits changes automatically

### 2. Documentation Validation (`validate-docs.yml`)

**Triggers:**
- All pushes and pull requests

**Actions:**
- Validates documentation structure
- Checks for broken internal links
- Validates problem directory structure
- Ensures markdown syntax correctness

### 3. Manual Update (`manual-update.yml`)

**Triggers:**
- Manual workflow dispatch

**Options:**
- Update type: `all`, `readme`, `index`, `performance`, `interview-prep`
- Force update: Update even if no changes detected

## 🛠️ Scripts

### `update_documentation.py`
Main documentation updater that:
- Scans all problem directories
- Extracts metadata from `Problem.md` files
- Detects available solution languages
- Updates all documentation files with new content

### `validate_documentation.py`
Validates documentation structure:
- Checks for required sections
- Validates markdown format
- Ensures consistency across files

### `check_links.py`
Validates internal links:
- Finds broken relative links
- Skips external URLs
- Reports missing referenced files

### `validate_problems.py`
Validates problem directory structure:
- Ensures `Problem.md` exists
- Checks for solution files
- Validates problem metadata format

## 🚀 How It Works

### Automatic Updates

1. **Detection**: When you push changes to problem directories, the workflow detects modified files
2. **Scanning**: The script scans all problem directories and extracts metadata
3. **Update**: All documentation files are updated with new problem information
4. **Commit**: Changes are automatically committed with a descriptive message

### Adding New Problems

When you add a new problem:

1. Create the problem directory (e.g., `Daily_Problems/DailyProblem7/`)
2. Add `Problem.md` with proper format:
   ```markdown
   # 1234. Problem Title
   
   **Difficulty**: Medium
   **Topics**: Array, Dynamic Programming
   
   [Problem description...]
   ```
3. Add solution files (`InCPP.cpp`, `InJava.java`, etc.)
4. Push to repository
5. CI/CD automatically updates all documentation! 🎉

### Manual Updates

If you need to manually trigger updates:

1. Go to GitHub Actions tab
2. Select "Manual Documentation Update"
3. Click "Run workflow"
4. Choose update type and options
5. Click "Run workflow" button

## 📊 Monitoring

### GitHub Actions Dashboard
- View workflow runs and status
- Check validation results
- Monitor automatic updates

### Workflow Summaries
Each workflow provides detailed summaries:
- Files changed
- Problems detected
- Validation results
- Performance reports

## 🔧 Configuration

### Environment Variables
- `GITHUB_TOKEN`: Automatically provided by GitHub Actions
- No additional secrets required

### Permissions
Workflows have:
- `contents: write` - To commit documentation updates
- `pull-requests: write` - To comment on PRs

## 🛡️ Error Handling

### Validation Failures
- Broken links stop the workflow
- Missing required files generate warnings
- Structure violations are reported

### Update Failures
- Failed updates are logged
- Manual intervention may be required
- Rollback procedures available

## 🎯 Best Practices

### Problem Structure
Ensure each problem directory has:
- `Problem.md` with proper format
- At least one solution file
- Consistent naming conventions

### Commit Messages
Automatic commits include:
- Changed files list
- Problem numbers affected
- Timestamp and workflow info

### Review Process
- Validate changes before pushing
- Review auto-generated documentation
- Monitor workflow results

## 🚀 Benefits

### Automation
- ✅ Zero manual documentation maintenance
- ✅ Consistent formatting across all files
- ✅ Real-time updates when problems are added

### Quality Assurance
- ✅ Link validation prevents broken references
- ✅ Structure validation ensures consistency
- ✅ Automatic error detection and reporting

### Developer Experience
- ✅ Focus on problem-solving, not documentation
- ✅ Immediate feedback on changes
- ✅ Professional-quality repository maintenance

## 🔮 Future Enhancements

Planned improvements:
- Performance benchmark automation
- Test case validation
- Solution correctness checking
- Multi-language compilation testing
- Advanced metrics and analytics

---

**Happy Coding!** 🎉 The CI/CD pipeline ensures your repository stays perfectly organized and up-to-date automatically!
