# 🎨 Image Customization Guide

## Current Setup (Default)

The dashboard currently uses **online images** from icons8.com. This means:
- ✅ No additional files needed
- ✅ Works immediately
- ✅ Images load from the internet
- ⚠️ Requires internet connection to see images

## Option 1: Keep Using Online Images (Recommended for Beginners)

### Current Image URLs in app.py:

1. **Sidebar Brain Icon**:
   ```python
   st.sidebar.image("https://img.icons8.com/fluency/96/000000/brain.png", width=100)
   ```

2. **Home Page Mental Health Image**:
   ```python
   st.image("https://img.icons8.com/bubbles/200/000000/mental-health.png", width=200)
   ```

### To Change to Different Online Images:

1. Go to any free image website:
   - https://icons8.com
   - https://www.flaticon.com
   - https://www.freepik.com
   - https://unsplash.com

2. Find an image you like

3. Right-click → "Copy Image Address"

4. In `app.py`, replace the URL:
   ```python
   # Old
   st.sidebar.image("https://img.icons8.com/fluency/96/000000/brain.png", width=100)
   
   # New (with your image URL)
   st.sidebar.image("YOUR_COPIED_IMAGE_URL_HERE", width=100)
   ```

---

## Option 2: Use Local Images (Stored on Your Computer)

### Step 1: Create Assets Folder

In your project folder, create a new folder called `assets` or `images`:

```
mental-health-dashboard/
│
├── assets/                  ← Create this folder
│   ├── brain_icon.png      ← Add your images here
│   └── mental_health.png   ← Add your images here
│
├── app.py
├── requirements.txt
└── synthetic_mental_health_dataset__1_.csv
```

### Step 2: Add Your Images

1. Download or create images:
   - Brain icon (recommended size: 96x96 pixels or similar)
   - Mental health image (recommended size: 200x200 pixels or similar)

2. Save them in the `assets` folder with these names:
   - `brain_icon.png`
   - `mental_health.png`

### Step 3: Update app.py

Find these lines in `app.py` and change them:

#### Change 1: Sidebar Image
**Original (Line ~113):**
```python
st.sidebar.image("https://img.icons8.com/fluency/96/000000/brain.png", width=100)
```

**Change to:**
```python
st.sidebar.image("assets/brain_icon.png", width=100)
```

#### Change 2: Home Page Image
**Original (Line ~137):**
```python
st.image("https://img.icons8.com/bubbles/200/000000/mental-health.png", width=200)
```

**Change to:**
```python
st.image("assets/mental_health.png", width=200)
```

### Step 4: Save and Run

1. Save `app.py` (Ctrl+S or Cmd+S)
2. Restart your Streamlit app:
   ```bash
   streamlit run app.py
   ```

---

## Option 3: Mix Online and Local Images

You can use online images for some and local for others!

Example:
```python
# Use local image for sidebar
st.sidebar.image("assets/brain_icon.png", width=100)

# Use online image for home page
st.image("https://img.icons8.com/bubbles/200/000000/mental-health.png", width=200)
```

---

## Recommended Image Sizes

| Location | Recommended Size | Format |
|----------|-----------------|--------|
| Sidebar Icon | 96x96 to 128x128 px | PNG |
| Home Page Main Image | 200x200 to 400x400 px | PNG |
| Other Icons | 32x32 to 64x64 px | PNG |

---

## Free Image Resources

### Icons & Illustrations:
1. **Icons8** - https://icons8.com
   - Huge library of icons
   - Free with attribution
   - Search: "brain icon", "mental health"

2. **Flaticon** - https://www.flaticon.com
   - Vector icons
   - Free and premium options
   - PNG and SVG formats

3. **Freepik** - https://www.freepik.com
   - Icons and illustrations
   - Free with attribution

### Photos:
1. **Unsplash** - https://unsplash.com
   - High-quality photos
   - Completely free
   - No attribution required

2. **Pexels** - https://www.pexels.com
   - Free stock photos
   - Good mental health imagery

### Create Your Own:
1. **Canva** - https://www.canva.com
   - Create custom graphics
   - Free templates
   - Export as PNG

---

## Image Attribution (If Using Free Icons)

If you use free images from sites like Icons8 or Flaticon, you might need to add attribution.

Add this to the bottom of your sidebar in `app.py`:

```python
st.sidebar.markdown("---")
st.sidebar.caption("Icons by [Icons8](https://icons8.com)")
```

Or at the bottom of your conclusion page:

```python
st.markdown("---")
st.caption("Icons provided by [Icons8](https://icons8.com)")
```

---

## Troubleshooting Images

### ❌ Image doesn't show (using local images)
**Possible causes:**
1. Wrong file path
   - ✅ Check spelling: `assets/brain_icon.png`
   - ✅ Check folder exists
   - ✅ Check file is actually in folder

2. Wrong file format
   - ✅ Make sure it's PNG, JPG, or JPEG
   - ✅ Check file extension matches code

3. File permissions
   - ✅ Make sure file isn't locked/protected

**Solution:**
```python
# Add error handling
try:
    st.sidebar.image("assets/brain_icon.png", width=100)
except:
    st.sidebar.image("https://img.icons8.com/fluency/96/000000/brain.png", width=100)
```

### ❌ Online image doesn't load
**Possible causes:**
1. No internet connection
2. Image URL is broken
3. Website blocking direct image access

**Solution:** Use local images instead

### ❌ Image is too big/small
**Solution:** Adjust the `width` parameter:
```python
# Make smaller
st.sidebar.image("assets/brain_icon.png", width=50)

# Make larger  
st.sidebar.image("assets/brain_icon.png", width=150)

# Full width
st.image("assets/mental_health.png", use_column_width=True)
```

---

## Advanced: Using Different Image Formats

### SVG (Vector) Images
```python
# For local SVG
st.sidebar.image("assets/brain_icon.svg", width=100)

# SVG from URL
st.sidebar.image("https://example.com/icon.svg", width=100)
```

### GIF (Animated)
```python
st.image("assets/loading_animation.gif", width=200)
```

### WEBP (Modern format)
```python
st.image("assets/optimized_image.webp", width=200)
```

---

## Quick Reference

### Find the image code in app.py:

**Line numbers where images are used:**
- Line ~113: `st.sidebar.image(...)` - Sidebar icon
- Line ~137: `st.image(...)` - Home page main image

**To find them quickly in VS Code:**
- Press `Ctrl+F` (Windows/Linux) or `Cmd+F` (Mac)
- Search for: `st.sidebar.image` or `st.image`

---

## Example: Complete Local Image Setup

1. **Create folder:**
   ```
   mkdir assets
   ```

2. **Add images to assets folder:**
   - `brain_icon.png`
   - `mental_health.png`

3. **Update app.py (find and replace):**
   
   **Find:**
   ```python
   st.sidebar.image("https://img.icons8.com/fluency/96/000000/brain.png", width=100)
   ```
   **Replace with:**
   ```python
   st.sidebar.image("assets/brain_icon.png", width=100)
   ```
   
   **Find:**
   ```python
   st.image("https://img.icons8.com/bubbles/200/000000/mental-health.png", width=200)
   ```
   **Replace with:**
   ```python
   st.image("assets/mental_health.png", width=200)
   ```

4. **Save and test:**
   ```bash
   streamlit run app.py
   ```

---

**Pro Tip:** Start with online images (default setup) to get your dashboard working first. Add custom local images later once everything is running smoothly!

---

**Remember:** 
- PNG format is most compatible
- Keep images reasonably sized (under 1MB)
- Use descriptive filenames
- Test after every change
