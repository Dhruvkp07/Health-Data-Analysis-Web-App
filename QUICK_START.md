# 🚀 Quick Start Guide

## For Absolute Beginners

### What You Need:
1. Python installed on your computer
2. VS Code (or any text editor)
3. The files from this project

### Step-by-Step Setup:

#### 1️⃣ Create a Folder
Create a new folder on your desktop called `mental-health-dashboard`

#### 2️⃣ Add Files
Put these 3 files in that folder:
- `app.py` (the main code file)
- `requirements.txt` (list of tools needed)
- `synthetic_mental_health_dataset__1_.csv` (your data file)

#### 3️⃣ Open Terminal/Command Prompt
- **Windows**: Press `Win + R`, type `cmd`, press Enter
- **Mac**: Press `Cmd + Space`, type `terminal`, press Enter
- **Linux**: Press `Ctrl + Alt + T`

#### 4️⃣ Navigate to Your Folder
Type this command (replace with your actual folder location):
```bash
cd Desktop/mental-health-dashboard
```

#### 5️⃣ Install Required Tools
Copy and paste this command:
```bash
pip install -r requirements.txt
```
Wait for it to finish (might take 2-3 minutes)

#### 6️⃣ Run the Dashboard
Type this command:
```bash
streamlit run app.py
```

#### 7️⃣ Open in Browser
Your dashboard will automatically open in your web browser!
If not, go to: http://localhost:8501

---

## Using VS Code (Recommended)

### Easy Method:

1. **Open VS Code**
   
2. **Open Your Folder**
   - Click `File` → `Open Folder`
   - Select your `mental-health-dashboard` folder

3. **Create Files**
   - Right-click in sidebar → `New File`
   - Name it `app.py`
   - Paste the app code
   - Repeat for `requirements.txt`

4. **Open Terminal in VS Code**
   - Click `Terminal` → `New Terminal` (at top menu)
   - Terminal opens at bottom of screen

5. **Install Dependencies**
   Type in terminal:
   ```bash
   pip install -r requirements.txt
   ```

6. **Run Dashboard**
   Type in terminal:
   ```bash
   streamlit run app.py
   ```

---

## Adding Custom Images

### Method 1: Use Online Images (Easiest)

The code already uses online images from icons8.com - no setup needed!

### Method 2: Use Your Own Images

1. Create a folder called `assets` in your project folder

2. Add your images to the `assets` folder:
   - `brain_icon.png` (for sidebar)
   - `mental_health.png` (for home page)

3. In `app.py`, find these lines and change them:

**Original:**
```python
st.sidebar.image("https://img.icons8.com/fluency/96/000000/brain.png", width=100)
```

**Change to:**
```python
st.sidebar.image("assets/brain_icon.png", width=100)
```

**Original:**
```python
st.image("https://img.icons8.com/bubbles/200/000000/mental-health.png", width=200)
```

**Change to:**
```python
st.image("assets/mental_health.png", width=200)
```

### Where to Find Free Images:

- **Icons8**: https://icons8.com (free with attribution)
- **Flaticon**: https://www.flaticon.com (free with attribution)
- **Unsplash**: https://unsplash.com (completely free)
- **Pexels**: https://www.pexels.com (completely free)

To get image URL from these sites:
1. Right-click on image
2. Select "Copy image address" or "Copy image link"
3. Paste it in the code

---

## Common Issues & Solutions

### ❌ "Python is not recognized"
**Solution**: Install Python from python.org
- Download Python 3.8 or higher
- ✅ Check "Add Python to PATH" during installation

### ❌ "pip is not recognized"
**Solution**: Reinstall Python with "Add to PATH" checked

### ❌ "No module named 'streamlit'"
**Solution**: Run `pip install -r requirements.txt` again

### ❌ "File not found: synthetic_mental_health_dataset__1_.csv"
**Solution**: Make sure CSV file is in the same folder as app.py

### ❌ Dashboard doesn't open automatically
**Solution**: Manually open browser and go to http://localhost:8501

### ❌ "Address already in use"
**Solution**: Use different port:
```bash
streamlit run app.py --server.port 8502
```
Then open: http://localhost:8502

---

## Testing Your Dashboard

Once running, check these features:

✅ Home page loads with images  
✅ Sidebar navigation works  
✅ Can switch between pages  
✅ Dataset Overview shows data  
✅ EDA visualizations appear  
✅ Can train the model  
✅ Can make predictions with sliders  
✅ All tabs work properly  

---

## Tips for VS Code Users

### Helpful Extensions:
- **Python** (by Microsoft) - Essential for Python development
- **Pylance** - Better Python language support
- **Prettier** - Code formatting

### Useful VS Code Shortcuts:
- `Ctrl + S` (Windows/Linux) or `Cmd + S` (Mac) - Save file
- `Ctrl + `` ` - Open/close terminal
- `Ctrl + P` - Quick file search
- `F5` - Start debugging (if needed)

### View Multiple Files:
- Right-click on file → "Split Right"
- See your code and README side-by-side

---

## Next Steps After Setup

1. **Explore the Dashboard**
   - Click through all navigation pages
   - Try different visualizations
   - Test the prediction model

2. **Customize**
   - Change colors in the CSS section
   - Add your own insights
   - Modify text descriptions

3. **Learn**
   - Read through the code
   - Understand how Streamlit works
   - Experiment with changes

---

## Need Help?

**Check the README.md file for:**
- Detailed troubleshooting
- Feature explanations
- Customization options

**Common Resources:**
- Streamlit Docs: https://docs.streamlit.io
- Python Docs: https://docs.python.org
- Stack Overflow: https://stackoverflow.com

---

**Remember**: The first time setup might seem complex, but you only need to do it once! After that, running the dashboard is just one command: `streamlit run app.py`

Good luck! 🎉
