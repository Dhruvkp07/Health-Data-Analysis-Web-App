# 📂 File Structure & Organization Guide

## Complete Project Structure

Here's what your final project folder should look like:

```
mental-health-dashboard/
│
├── 📄 ESSENTIAL FILES (Required to run)
│   ├── app.py                                    # Main Streamlit application (REQUIRED)
│   ├── requirements.txt                          # Python dependencies (REQUIRED)
│   └── synthetic_mental_health_dataset__1_.csv   # Your dataset (REQUIRED)
│
├── 📖 DOCUMENTATION FILES (Helpful guides)
│   ├── README.md                                 # Main project documentation
│   ├── QUICK_START.md                           # Beginner setup guide
│   ├── IMAGE_GUIDE.md                           # Image customization help
│   ├── CHECKLIST.md                             # Deployment checklist
│   └── FILE_STRUCTURE.md                        # This file
│
├── 🧪 TESTING & UTILITIES
│   └── test_setup.py                            # Setup verification script
│
├── 🎨 ASSETS (Optional - if using local images)
│   ├── brain_icon.png                           # Sidebar icon
│   └── mental_health.png                        # Home page image
│
└── ⚙️ CONFIGURATION (Optional)
    └── .gitignore                                # For GitHub/version control

```

---

## File Descriptions

### 🔴 REQUIRED FILES (Cannot run without these)

#### 1. `app.py` (Main Application)
- **Size:** ~45 KB
- **Type:** Python script
- **Purpose:** The complete Streamlit dashboard application
- **Contains:**
  - Home page
  - Dataset overview page
  - EDA & insights page
  - Prediction model page
  - Conclusion page
  - All visualizations
  - Machine learning model
  - Navigation logic

**How to use:**
```bash
streamlit run app.py
```

---

#### 2. `requirements.txt` (Dependencies)
- **Size:** ~200 bytes
- **Type:** Text file
- **Purpose:** Lists all Python packages needed
- **Contains:**
  ```
  streamlit==1.28.0
  pandas==2.0.3
  numpy==1.24.3
  matplotlib==3.7.2
  seaborn==0.12.2
  plotly==5.17.0
  scikit-learn==1.3.0
  ```

**How to use:**
```bash
pip install -r requirements.txt
```

---

#### 3. `synthetic_mental_health_dataset__1_.csv` (Data)
- **Size:** ~269 KB
- **Type:** CSV (Comma-Separated Values)
- **Purpose:** Your mental health dataset
- **Contains:** 12 columns with lifestyle and mental health data

**Columns:**
- sleep_hours
- screen_time
- exercise_minutes
- daily_pending_tasks
- interruptions
- fatigue_level
- social_hours
- coffee_cups
- diet_quality
- weather
- mood_score
- stress_level

---

### 🟢 DOCUMENTATION FILES (Helpful but optional)

#### 4. `README.md` (Main Documentation)
- **Size:** ~8 KB
- **Purpose:** Complete project documentation
- **Contains:**
  - Project overview
  - Features list
  - Setup instructions
  - Troubleshooting guide
  - Dataset information

**When to read:** Before starting setup

---

#### 5. `QUICK_START.md` (Beginner Guide)
- **Size:** ~12 KB
- **Purpose:** Step-by-step setup for beginners
- **Contains:**
  - Absolute beginner instructions
  - VS Code specific guide
  - Common issues and solutions
  - Image setup basics

**When to read:** If you're new to Python/Streamlit

---

#### 6. `IMAGE_GUIDE.md` (Image Help)
- **Size:** ~15 KB
- **Purpose:** Complete guide for customizing images
- **Contains:**
  - Online vs local images
  - How to use custom images
  - Free image resources
  - Troubleshooting image issues

**When to read:** When you want to change dashboard images

---

#### 7. `CHECKLIST.md` (Deployment Guide)
- **Size:** ~10 KB
- **Purpose:** Pre-deployment verification
- **Contains:**
  - Setup checklist
  - Feature testing steps
  - Performance checks
  - Sharing options

**When to read:** Before presenting/deploying

---

#### 8. `FILE_STRUCTURE.md` (This File)
- **Purpose:** Explains all project files
- **Contains:**
  - File organization
  - File descriptions
  - Usage instructions

**When to read:** To understand project organization

---

### 🟡 TESTING FILES

#### 9. `test_setup.py` (Setup Tester)
- **Size:** ~5 KB
- **Purpose:** Verify your setup is correct
- **Tests:**
  - Python version
  - Package installations
  - Data file presence
  - App file existence

**How to use:**
```bash
python test_setup.py
```

---

### 🟣 OPTIONAL FILES

#### 10. `.gitignore` (Version Control)
- **Size:** ~500 bytes
- **Purpose:** Tells Git which files to ignore
- **Use when:** Uploading to GitHub/GitLab

---

#### 11. `assets/` folder (Custom Images)
- **Purpose:** Store local image files
- **Create when:** Using custom images instead of online ones
- **Contains:**
  - `brain_icon.png` - Sidebar icon
  - `mental_health.png` - Home page image
  - Any other custom images

---

## File Relationships

```
app.py
  ↓ reads
synthetic_mental_health_dataset__1_.csv
  ↓ uses packages from
requirements.txt
  ↓ optionally loads
assets/brain_icon.png
assets/mental_health.png
```

---

## Which Files Do You Need?

### Minimum Setup (Just to run locally)
```
✅ app.py
✅ requirements.txt
✅ synthetic_mental_health_dataset__1_.csv
```

### Recommended Setup (With documentation)
```
✅ app.py
✅ requirements.txt
✅ synthetic_mental_health_dataset__1_.csv
✅ README.md
✅ QUICK_START.md
```

### Complete Setup (Everything)
```
✅ All files listed above
```

### For GitHub Upload
```
✅ All files
✅ .gitignore
```

---

## File Sizes Reference

| File | Approximate Size |
|------|------------------|
| app.py | 45 KB |
| requirements.txt | 200 bytes |
| CSV data | 269 KB |
| README.md | 8 KB |
| QUICK_START.md | 12 KB |
| IMAGE_GUIDE.md | 15 KB |
| CHECKLIST.md | 10 KB |
| FILE_STRUCTURE.md | 8 KB |
| test_setup.py | 5 KB |
| .gitignore | 500 bytes |
| **Total** | **~373 KB** |

---

## How to Create This Structure in VS Code

### Method 1: Manual Creation

1. **Create project folder:**
   ```
   Right-click > New Folder > "mental-health-dashboard"
   ```

2. **Open in VS Code:**
   ```
   File > Open Folder > Select "mental-health-dashboard"
   ```

3. **Create each file:**
   ```
   Right-click in sidebar > New File > Type filename
   Paste content > Save (Ctrl+S)
   ```

### Method 2: Using Terminal

```bash
# Create folder
mkdir mental-health-dashboard
cd mental-health-dashboard

# Create files
touch app.py
touch requirements.txt
touch README.md
touch QUICK_START.md
touch IMAGE_GUIDE.md
touch CHECKLIST.md
touch FILE_STRUCTURE.md
touch test_setup.py
touch .gitignore

# Create assets folder
mkdir assets

# Then paste content into each file
```

---

## Organizing Your Files

### Good Organization ✅
```
mental-health-dashboard/
├── app.py
├── requirements.txt
├── synthetic_mental_health_dataset__1_.csv
├── README.md
└── assets/
    └── brain_icon.png
```

### Bad Organization ❌
```
Downloads/
├── app.py
Documents/
├── requirements.txt
Desktop/
├── synthetic_mental_health_dataset__1_.csv
```

**Why?** All files must be in the SAME folder!

---

## File Naming Rules

### ✅ Good Filenames
- `app.py` (lowercase, no spaces)
- `requirements.txt` (descriptive)
- `synthetic_mental_health_dataset__1_.csv` (as provided)

### ❌ Bad Filenames
- `App.py` (wrong case)
- `my app.py` (has space)
- `data.csv` (not descriptive enough)

---

## Backup Strategy

### What to Backup
✅ Entire project folder  
✅ Original CSV data  
✅ Modified app.py (if you customized)

### How to Backup
1. **Local backup:**
   - Copy entire folder
   - Paste to external drive/cloud

2. **GitHub backup:**
   - Create repository
   - Upload all files
   - Commit changes regularly

3. **Cloud backup:**
   - Google Drive
   - Dropbox
   - OneDrive

---

## Working with Multiple Versions

### Version Naming
```
mental-health-dashboard/        # Current version
mental-health-dashboard-v1/     # Backup version
mental-health-dashboard-final/  # Final version
```

### Or use Git branches:
```bash
git checkout -b custom-colors
git checkout -b add-features
git checkout main  # Original version
```

---

## File Modification Tips

### Before Modifying ANY File:
1. ✅ Make a backup copy
2. ✅ Test the original works
3. ✅ Make small changes
4. ✅ Test after each change

### If Something Breaks:
1. Check error message
2. Undo last change
3. Restore from backup
4. Start fresh if needed

---

## Quick Reference

### To Run Dashboard:
```bash
streamlit run app.py
```

### To Test Setup:
```bash
python test_setup.py
```

### To Install Packages:
```bash
pip install -r requirements.txt
```

### To Check Files:
```bash
ls                    # Mac/Linux
dir                   # Windows
```

---

## Need Help Finding Files?

### In VS Code:
- Press `Ctrl+P` (Windows/Linux) or `Cmd+P` (Mac)
- Type filename
- Press Enter

### In Terminal:
```bash
# Find a file
find . -name "app.py"

# List all files
ls -la               # Mac/Linux
dir /a               # Windows
```

---

## File Checklist Before Running

Use this checklist to verify everything is ready:

```
□ All files in same folder
□ CSV filename matches exactly
□ app.py contains complete code
□ requirements.txt has all packages
□ No typos in filenames
□ Files are saved (not just open)
□ Working directory is correct
```

---

**Pro Tip:** Keep all your project files organized in ONE folder. This makes everything simpler and prevents "file not found" errors!

**Remember:** The only truly required files are `app.py`, `requirements.txt`, and `synthetic_mental_health_dataset__1_.csv`. Everything else is helpful documentation!
