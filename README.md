# 🧠 Mental Health Analytics Dashboard

An interactive Streamlit dashboard for analyzing lifestyle factors and their impact on mental health using machine learning.

## 📋 Project Overview

This dashboard provides comprehensive insights into how daily habits like sleep, exercise, screen time, and diet affect mental wellbeing. It includes exploratory data analysis, interactive visualizations, and a machine learning model to predict stress levels.

## 🚀 Features

- **Home Page**: Project overview and introduction
- **Dataset Overview**: Explore data statistics and structure
- **EDA & Insights**: Interactive visualizations and pattern analysis
- **Prediction Model**: ML-powered stress level prediction
- **Conclusion**: Key findings and recommendations

## 📁 Project Structure

```
mental-health-dashboard/
│
├── app.py                                      # Main Streamlit application
├── requirements.txt                            # Python dependencies
├── synthetic_mental_health_dataset__1_.csv    # Dataset file
└── README.md                                  # This file
```

## 🛠️ Setup Instructions

### Step 1: Install Python
Make sure you have Python 3.8 or higher installed on your system.

### Step 2: Create Project Folder
Create a new folder for your project and navigate to it:
```bash
mkdir mental-health-dashboard
cd mental-health-dashboard
```

### Step 3: Copy Files
Copy the following files into your project folder:
- `app.py` (main application file)
- `requirements.txt` (dependencies)
- `synthetic_mental_health_dataset__1_.csv` (your dataset)

### Step 4: Install Dependencies
Open terminal/command prompt in your project folder and run:
```bash
pip install -r requirements.txt
```

### Step 5: Run the Dashboard
Execute the following command:
```bash
streamlit run app.py
```

The dashboard will automatically open in your default web browser at `http://localhost:8501`

## 💻 Using VS Code

1. Open VS Code
2. Open your project folder (File > Open Folder)
3. Create new files and paste the code:
   - Create `app.py` and paste the main app code
   - Create `requirements.txt` and paste dependencies
   - Add your CSV file to the same folder
4. Open terminal in VS Code (Terminal > New Terminal)
5. Run: `pip install -r requirements.txt`
6. Run: `streamlit run app.py`

## 📊 Dataset Information

The dataset includes the following features:
- **sleep_hours**: Daily sleep duration
- **screen_time**: Hours on digital devices
- **exercise_minutes**: Physical activity time
- **daily_pending_tasks**: Number of pending tasks
- **interruptions**: Frequency of disruptions
- **fatigue_level**: Tiredness level (0-10)
- **social_hours**: Social interaction time
- **coffee_cups**: Daily coffee consumption
- **diet_quality**: Nutritional quality (poor/average/good)
- **weather**: Daily weather conditions
- **mood_score**: Mood rating (0-10)
- **stress_level**: Stress intensity (0-10)

## 🎨 Customizing Images

The dashboard uses online images from icons8.com. To use your own images:

1. **Option 1 - Use online images:**
   - Find images on websites like icons8.com, flaticon.com, or similar
   - Copy the image URL
   - Replace the URLs in `app.py`:
     ```python
     st.sidebar.image("YOUR_IMAGE_URL_HERE", width=100)
     ```

2. **Option 2 - Use local images:**
   - Create an `assets` or `images` folder in your project
   - Add your images to this folder
   - Update the code:
     ```python
     st.sidebar.image("assets/brain_icon.png", width=100)
     st.image("assets/mental_health.png", width=200)
     ```

3. **Current image URLs in the code:**
   - Sidebar brain icon: `https://img.icons8.com/fluency/96/000000/brain.png`
   - Home page image: `https://img.icons8.com/bubbles/200/000000/mental-health.png`

## 🔧 Troubleshooting

**Error: Module not found**
- Solution: Make sure you installed all requirements: `pip install -r requirements.txt`

**Error: File not found (CSV)**
- Solution: Ensure the CSV file is in the same folder as `app.py`

**Port already in use**
- Solution: Run with different port: `streamlit run app.py --server.port 8502`

**Slow performance**
- Solution: The model training might take a few seconds. This is normal.

## 📱 Features Breakdown

### Interactive Elements
- Sliders for inputting lifestyle data
- Dropdown menus for navigation
- Interactive plots (zoom, pan, hover for details)
- Real-time predictions

### Visualizations
- Distribution plots
- Correlation heatmaps
- Scatter plots with trendlines
- Box plots
- Bar charts
- Confusion matrix

### Machine Learning
- Random Forest Classifier
- 80-20 train-test split
- Feature scaling with StandardScaler
- Model evaluation metrics
- Feature importance analysis

## 🎓 Learning Outcomes

This project demonstrates:
- Data analysis and visualization
- Machine learning implementation
- Web dashboard development
- User interface design
- Statistical interpretation
- Health data analytics

## 📝 Notes

- The dashboard is designed to be user-friendly for non-technical audiences
- All visualizations include explanatory text
- Medical/health terminology is explained in simple language
- Predictions are educational and not medical advice

## 🤝 Support

If you encounter any issues:
1. Check that all files are in the correct location
2. Verify Python version (3.8+)
3. Ensure all dependencies are installed
4. Check the terminal for error messages

## 📄 License

This project is for educational purposes.

---

**Created by:** Data Science Student  
**Technologies Used:** Python, Streamlit, Pandas, Scikit-learn, Plotly  
**Last Updated:** 2026
