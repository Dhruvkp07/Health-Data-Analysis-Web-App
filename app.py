import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import warnings
warnings.filterwarnings('ignore')

# Page Configuration
st.set_page_config(
    page_title="Mental Health Analytics Dashboard",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #4CAF50;
    }
    h1 {
        color: #2C3E50;
    }
    h2 {
        color: #34495E;
    }
    h3 {
        color: #5D6D7E;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 10px 20px;
        background-color: #f0f2f6;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('synthetic_mental_health_dataset__1_.csv')
    return df

# Sidebar Navigation
def sidebar_navigation():
    st.sidebar.image("https://img.icons8.com/fluency/96/000000/brain.png", width=100)
    st.sidebar.title("🧠 Mental Health Analytics")
    st.sidebar.markdown("---")
    
    page = st.sidebar.radio(
        "Navigate to:",
        ["🏠 Home", "📊 Dataset Overview", "📈 EDA & Insights", "🤖 Prediction Model", "📝 Conclusion"]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.info("""
    **About this Dashboard:**
    
    This interactive dashboard analyzes lifestyle factors and their impact on mental health. 
    Explore data patterns, visualizations, and use ML models to predict stress levels.
    """)
    
    return page

# Home Page
def home_page():
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.image("https://img.icons8.com/bubbles/200/000000/mental-health.png", width=200)
        st.title("Mental Health Analytics Dashboard")
        st.markdown("### Understanding the Connection Between Lifestyle and Mental Wellbeing")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ## 🎯 Project Overview
        
        Mental health is deeply influenced by our daily habits and lifestyle choices. This dashboard explores 
        how factors like sleep, exercise, screen time, and diet affect our mental wellbeing.
        
        **What you'll discover:**
        - How sleep patterns impact mood and stress
        - The relationship between exercise and mental health
        - Effects of screen time on fatigue levels
        - Dietary influences on stress and mood
        - Weather's surprising role in mental wellbeing
        """)
    
    with col2:
        st.markdown("""
        ## 📋 Dataset Features
        
        Our analysis includes data on:
        - **Sleep Hours**: Daily sleep duration
        - **Screen Time**: Hours spent on digital devices
        - **Exercise Minutes**: Physical activity duration
        - **Pending Tasks**: Daily workload indicators
        - **Interruptions**: Frequency of disruptions
        - **Social Hours**: Time spent socializing
        - **Coffee Consumption**: Daily cups consumed
        - **Diet Quality**: Nutritional quality (poor/average/good)
        - **Weather Conditions**: Environmental factors
        - **Mood & Stress Levels**: Mental health outcomes
        """)
    
    st.markdown("---")
    
    st.markdown("## 🚀 How to Use This Dashboard")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.info("**📊 Dataset Overview**\n\nExplore the basic statistics and structure of the data")
    
    with col2:
        st.info("**📈 EDA & Insights**\n\nVisualize patterns and relationships in the data")
    
    with col3:
        st.info("**🤖 Prediction Model**\n\nPredict stress levels using machine learning")
    
    with col4:
        st.info("**📝 Conclusion**\n\nKey findings and recommendations")

# Dataset Overview Page
def dataset_overview_page(df):
    st.title("📊 Dataset Overview")
    st.markdown("### Let's explore what our data looks like")
    
    st.markdown("---")
    
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Records", f"{len(df):,}")
    with col2:
        st.metric("Features", len(df.columns))
    with col3:
        st.metric("Average Mood Score", f"{df['mood_score'].mean():.2f}")
    with col4:
        st.metric("Average Stress Level", f"{df['stress_level'].mean():.2f}")
    
    st.markdown("---")
    
    # Data Preview
    st.subheader("📋 Sample Data")
    st.dataframe(df.head(10), use_container_width=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Statistical Summary")
        st.dataframe(df.describe(), use_container_width=True)
    
    with col2:
        st.subheader("🔍 Data Information")
        
        # Create info dataframe
        info_data = {
            'Column': df.columns,
            'Data Type': df.dtypes.values,
            'Non-Null Count': [df[col].count() for col in df.columns],
            'Null Count': [df[col].isnull().sum() for col in df.columns]
        }
        info_df = pd.DataFrame(info_data)
        st.dataframe(info_df, use_container_width=True)
    
    st.markdown("---")
    
    # Missing Values Check
    st.subheader("🔎 Data Quality Check")
    missing_data = df.isnull().sum()
    if missing_data.sum() == 0:
        st.success("✅ Great news! The dataset has no missing values. All records are complete!")
    else:
        fig = px.bar(x=missing_data.index, y=missing_data.values,
                     labels={'x': 'Columns', 'y': 'Missing Values'},
                     title='Missing Values by Column')
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Feature Descriptions
    st.subheader("📚 Feature Descriptions")
    
    feature_desc = {
        "sleep_hours": "Average daily sleep duration in hours",
        "screen_time": "Daily hours spent on digital devices",
        "exercise_minutes": "Time spent on physical activities per day",
        "daily_pending_tasks": "Number of incomplete tasks each day",
        "interruptions": "Frequency of work/study disruptions",
        "fatigue_level": "Self-reported tiredness level (0-10)",
        "social_hours": "Time spent in social interactions",
        "coffee_cups": "Number of coffee cups consumed daily",
        "diet_quality": "Overall nutritional quality (poor/average/good)",
        "weather": "Daily weather conditions",
        "mood_score": "Self-reported mood rating (0-10)",
        "stress_level": "Self-reported stress intensity (0-10)"
    }
    
    desc_df = pd.DataFrame(list(feature_desc.items()), columns=['Feature', 'Description'])
    st.table(desc_df)

# EDA & Insights Page
def eda_insights_page(df):
    st.title("📈 Exploratory Data Analysis & Insights")
    st.markdown("### Discovering patterns and relationships in mental health data")
    
    st.markdown("---")
    
    # Tabs for different analysis
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Distribution Analysis", "🔗 Correlations", "🎯 Factor Analysis", "🌦️ Environmental Impact"])
    
    with tab1:
        st.subheader("Distribution of Key Features")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Sleep Hours Distribution
            fig = px.histogram(df, x='sleep_hours', nbins=30,
                             title='Sleep Hours Distribution',
                             labels={'sleep_hours': 'Hours of Sleep'},
                             color_discrete_sequence=['#3498db'])
            fig.add_vline(x=df['sleep_hours'].mean(), line_dash="dash", 
                         annotation_text=f"Average: {df['sleep_hours'].mean():.2f}h")
            st.plotly_chart(fig, use_container_width=True)
            
            st.info(f"""
            **Insight:** The average sleep duration is {df['sleep_hours'].mean():.2f} hours. 
            Most people sleep between {df['sleep_hours'].quantile(0.25):.1f} and {df['sleep_hours'].quantile(0.75):.1f} hours. 
            {'This is within healthy ranges!' if 7 <= df['sleep_hours'].mean() <= 9 else 'Consider aiming for 7-9 hours for optimal health.'}
            """)
        
        with col2:
            # Mood Score Distribution
            fig = px.histogram(df, x='mood_score', nbins=30,
                             title='Mood Score Distribution',
                             labels={'mood_score': 'Mood Score (0-10)'},
                             color_discrete_sequence=['#2ecc71'])
            fig.add_vline(x=df['mood_score'].mean(), line_dash="dash",
                         annotation_text=f"Average: {df['mood_score'].mean():.2f}")
            st.plotly_chart(fig, use_container_width=True)
            
            st.info(f"""
            **Insight:** The average mood score is {df['mood_score'].mean():.2f} out of 10. 
            {'Most people report positive mood levels!' if df['mood_score'].mean() > 6 else 'There might be room for improvement in overall wellbeing.'}
            """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Stress Level Distribution
            fig = px.histogram(df, x='stress_level', nbins=30,
                             title='Stress Level Distribution',
                             labels={'stress_level': 'Stress Level (0-10)'},
                             color_discrete_sequence=['#e74c3c'])
            fig.add_vline(x=df['stress_level'].mean(), line_dash="dash",
                         annotation_text=f"Average: {df['stress_level'].mean():.2f}")
            st.plotly_chart(fig, use_container_width=True)
            
            st.warning(f"""
            **Insight:** Average stress level is {df['stress_level'].mean():.2f}. 
            {'Stress levels appear moderate across the population.' if df['stress_level'].mean() < 5 else 'Elevated stress levels detected - lifestyle interventions may help.'}
            """)
        
        with col2:
            # Screen Time Distribution
            fig = px.histogram(df, x='screen_time', nbins=30,
                             title='Screen Time Distribution',
                             labels={'screen_time': 'Screen Time (hours)'},
                             color_discrete_sequence=['#9b59b6'])
            fig.add_vline(x=df['screen_time'].mean(), line_dash="dash",
                         annotation_text=f"Average: {df['screen_time'].mean():.2f}h")
            st.plotly_chart(fig, use_container_width=True)
            
            st.info(f"""
            **Insight:** Average screen time is {df['screen_time'].mean():.2f} hours per day. 
            {'This is within reasonable limits.' if df['screen_time'].mean() < 6 else 'Consider reducing screen time for better mental health.'}
            """)
    
    with tab2:
        st.subheader("Correlation Analysis")
        
        # Calculate correlation matrix
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        corr_matrix = df[numeric_cols].corr()
        
        # Heatmap
        fig = px.imshow(corr_matrix,
                       labels=dict(color="Correlation"),
                       x=corr_matrix.columns,
                       y=corr_matrix.columns,
                       color_continuous_scale='RdBu_r',
                       aspect='auto',
                       title='Correlation Heatmap - How Features Relate to Each Other')
        fig.update_layout(height=600)
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("---")
        
        # Key correlations
        st.subheader("🔑 Key Findings from Correlations")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Factors Positively Correlated with Mood:**")
            mood_corr = corr_matrix['mood_score'].sort_values(ascending=False)[1:6]
            for feature, corr in mood_corr.items():
                if corr > 0:
                    st.success(f"✅ {feature.replace('_', ' ').title()}: {corr:.3f}")
        
        with col2:
            st.markdown("**Factors Positively Correlated with Stress:**")
            stress_corr = corr_matrix['stress_level'].sort_values(ascending=False)[1:6]
            for feature, corr in stress_corr.items():
                if corr > 0:
                    st.error(f"⚠️ {feature.replace('_', ' ').title()}: {corr:.3f}")
    
    with tab3:
        st.subheader("Impact of Lifestyle Factors")
        
        # Sleep vs Mood
        fig1 = px.scatter(df, x='sleep_hours', y='mood_score',
                         title='Sleep Hours vs Mood Score',
                         labels={'sleep_hours': 'Hours of Sleep', 'mood_score': 'Mood Score'},
                         trendline='ols',
                         color='stress_level',
                         color_continuous_scale='Reds')
        st.plotly_chart(fig1, use_container_width=True)
        
        st.success("""
        **What this tells us:** People who sleep more tend to have better mood scores. 
        The colored points show stress levels - notice how higher stress (darker red) often 
        appears with less sleep and lower mood scores.
        """)
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Exercise vs Stress
            fig2 = px.scatter(df, x='exercise_minutes', y='stress_level',
                            title='Exercise vs Stress Level',
                            labels={'exercise_minutes': 'Exercise (minutes)', 'stress_level': 'Stress Level'},
                            trendline='ols',
                            color_discrete_sequence=['#3498db'])
            st.plotly_chart(fig2, use_container_width=True)
            
            st.info("**Takeaway:** Regular exercise appears to be associated with lower stress levels!")
        
        with col2:
            # Screen Time vs Fatigue
            fig3 = px.scatter(df, x='screen_time', y='fatigue_level',
                            title='Screen Time vs Fatigue Level',
                            labels={'screen_time': 'Screen Time (hours)', 'fatigue_level': 'Fatigue Level'},
                            trendline='ols',
                            color_discrete_sequence=['#e74c3c'])
            st.plotly_chart(fig3, use_container_width=True)
            
            st.warning("**Takeaway:** More screen time correlates with higher fatigue levels!")
        
        st.markdown("---")
        
        # Diet Quality Impact
        st.subheader("🥗 Diet Quality Impact on Mental Health")
        
        diet_mood = df.groupby('diet_quality')[['mood_score', 'stress_level']].mean().reset_index()
        
        fig4 = go.Figure()
        fig4.add_trace(go.Bar(name='Mood Score', x=diet_mood['diet_quality'], 
                             y=diet_mood['mood_score'], marker_color='#2ecc71'))
        fig4.add_trace(go.Bar(name='Stress Level', x=diet_mood['diet_quality'], 
                             y=diet_mood['stress_level'], marker_color='#e74c3c'))
        fig4.update_layout(title='Diet Quality vs Mental Health Metrics',
                          xaxis_title='Diet Quality',
                          yaxis_title='Score',
                          barmode='group')
        st.plotly_chart(fig4, use_container_width=True)
        
        st.success(f"""
        **Key Insight:** People with good diet quality have an average mood score of 
        {diet_mood[diet_mood['diet_quality']=='good']['mood_score'].values[0]:.2f} compared to 
        {diet_mood[diet_mood['diet_quality']=='poor']['mood_score'].values[0]:.2f} for those with poor diet. 
        Better nutrition really does make a difference!
        """)
    
    with tab4:
        st.subheader("🌦️ Environmental Factors")
        
        # Weather Impact
        weather_stats = df.groupby('weather')[['mood_score', 'stress_level', 'fatigue_level']].mean().reset_index()
        
        fig5 = go.Figure()
        fig5.add_trace(go.Bar(name='Mood Score', x=weather_stats['weather'], 
                             y=weather_stats['mood_score'], marker_color='#f39c12'))
        fig5.add_trace(go.Bar(name='Stress Level', x=weather_stats['weather'], 
                             y=weather_stats['stress_level'], marker_color='#3498db'))
        fig5.add_trace(go.Bar(name='Fatigue Level', x=weather_stats['weather'], 
                             y=weather_stats['fatigue_level'], marker_color='#95a5a6'))
        fig5.update_layout(title='Weather Conditions vs Mental Health',
                          xaxis_title='Weather',
                          yaxis_title='Score',
                          barmode='group')
        st.plotly_chart(fig5, use_container_width=True)
        
        best_weather = weather_stats.loc[weather_stats['mood_score'].idxmax(), 'weather']
        worst_weather = weather_stats.loc[weather_stats['stress_level'].idxmax(), 'weather']
        
        st.info(f"""
        **Weather Insights:**
        - Best weather for mood: {best_weather.title()} ☀️
        - Most stressful weather: {worst_weather.title()} ⚠️
        - Weather does affect our mental state, but remember it's just one factor among many!
        """)
        
        st.markdown("---")
        
        # Coffee Consumption Analysis
        st.subheader("☕ Coffee Consumption Patterns")
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig6 = px.box(df, x='coffee_cups', y='fatigue_level',
                         title='Coffee Consumption vs Fatigue',
                         labels={'coffee_cups': 'Cups of Coffee', 'fatigue_level': 'Fatigue Level'},
                         color='coffee_cups')
            st.plotly_chart(fig6, use_container_width=True)
        
        with col2:
            fig7 = px.box(df, x='coffee_cups', y='stress_level',
                         title='Coffee Consumption vs Stress',
                         labels={'coffee_cups': 'Cups of Coffee', 'stress_level': 'Stress Level'},
                         color='coffee_cups')
            st.plotly_chart(fig7, use_container_width=True)
        
        st.warning("""
        **Coffee Insight:** While coffee can help with alertness, too much caffeine might 
        increase stress levels. Moderation is key!
        """)

# Prediction Model Page
def prediction_model_page(df):
    st.title("🤖 Stress Level Prediction Model")
    st.markdown("### Using Machine Learning to Predict Stress Levels")
    
    st.markdown("---")
    
    tab1, tab2, tab3 = st.tabs(["📊 Model Training", "🎯 Make Predictions", "📈 Model Performance"])
    
    with tab1:
        st.subheader("How the Model Works")
        
        st.markdown("""
        Our machine learning model uses a **Random Forest Classifier** to predict stress levels based on lifestyle factors.
        
        **What is Random Forest?**
        Think of it as asking advice from many experts (trees) and taking the majority vote. 
        Each expert looks at your lifestyle factors and predicts your stress level, then we combine all their opinions!
        
        **Features used for prediction:**
        - Sleep hours
        - Screen time
        - Exercise minutes
        - Daily pending tasks
        - Interruptions
        - Fatigue level
        - Social hours
        - Coffee consumption
        """)
        
        st.markdown("---")
        
        if st.button("🚀 Train Model", key="train_model"):
            with st.spinner("Training the model... This might take a moment!"):
                # Prepare data
                df_model = df.copy()
                
                # Create stress categories
                df_model['stress_category'] = pd.cut(df_model['stress_level'], 
                                                      bins=[0, 2, 4, 6, 10],
                                                      labels=['Low', 'Moderate', 'High', 'Very High'])
                
                # Features
                feature_cols = ['sleep_hours', 'screen_time', 'exercise_minutes', 
                               'daily_pending_tasks', 'interruptions', 'fatigue_level',
                               'social_hours', 'coffee_cups']
                
                X = df_model[feature_cols]
                y = df_model['stress_category']
                
                # Split data
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
                
                # Scale features
                scaler = StandardScaler()
                X_train_scaled = scaler.fit_transform(X_train)
                X_test_scaled = scaler.transform(X_test)
                
                # Train model
                model = RandomForestClassifier(n_estimators=100, random_state=42)
                model.fit(X_train_scaled, y_train)
                
                # Predictions
                y_pred = model.predict(X_test_scaled)
                
                # Accuracy
                accuracy = accuracy_score(y_test, y_pred)
                
                # Store in session state
                st.session_state['model'] = model
                st.session_state['scaler'] = scaler
                st.session_state['accuracy'] = accuracy
                st.session_state['y_test'] = y_test
                st.session_state['y_pred'] = y_pred
                st.session_state['feature_cols'] = feature_cols
                
                st.success(f"✅ Model trained successfully! Accuracy: {accuracy*100:.2f}%")
                
                # Feature importance
                feature_importance = pd.DataFrame({
                    'feature': feature_cols,
                    'importance': model.feature_importances_
                }).sort_values('importance', ascending=False)
                
                fig = px.bar(feature_importance, x='importance', y='feature',
                            orientation='h',
                            title='Feature Importance - Which Factors Matter Most?',
                            labels={'importance': 'Importance Score', 'feature': 'Lifestyle Factor'},
                            color='importance',
                            color_continuous_scale='Viridis')
                st.plotly_chart(fig, use_container_width=True)
                
                st.info(f"""
                **What this means:** The '{feature_importance.iloc[0]['feature'].replace('_', ' ').title()}' 
                is the most important factor in predicting stress levels according to our model!
                """)
    
    with tab2:
        st.subheader("🎯 Predict Your Stress Level")
        
        if 'model' not in st.session_state:
            st.warning("⚠️ Please train the model first in the 'Model Training' tab!")
        else:
            st.markdown("Enter your lifestyle information below to predict your stress level:")
            
            col1, col2 = st.columns(2)
            
            with col1:
                sleep_hours = st.slider("Sleep Hours", 0.0, 12.0, 7.0, 0.5)
                screen_time = st.slider("Screen Time (hours)", 0.0, 15.0, 4.0, 0.5)
                exercise_minutes = st.slider("Exercise Minutes", 0, 180, 30, 5)
                daily_tasks = st.slider("Daily Pending Tasks", 0, 10, 3, 1)
            
            with col2:
                interruptions = st.slider("Interruptions", 0, 15, 5, 1)
                fatigue_level = st.slider("Fatigue Level (0-10)", 0.0, 10.0, 5.0, 0.5)
                social_hours = st.slider("Social Hours", 0.0, 10.0, 2.0, 0.5)
                coffee_cups = st.slider("Coffee Cups", 0, 10, 2, 1)
            
            if st.button("🔮 Predict Stress Level", key="predict_button"):
                # Prepare input
                input_data = np.array([[sleep_hours, screen_time, exercise_minutes,
                                       daily_tasks, interruptions, fatigue_level,
                                       social_hours, coffee_cups]])
                
                # Scale input
                input_scaled = st.session_state['scaler'].transform(input_data)
                
                # Predict
                prediction = st.session_state['model'].predict(input_scaled)[0]
                probabilities = st.session_state['model'].predict_proba(input_scaled)[0]
                
                # Display result
                st.markdown("---")
                st.subheader("Prediction Results")
                
                # Color based on prediction
                if prediction == 'Low':
                    st.success(f"### Predicted Stress Level: {prediction} 😊")
                elif prediction == 'Moderate':
                    st.info(f"### Predicted Stress Level: {prediction} 😐")
                elif prediction == 'High':
                    st.warning(f"### Predicted Stress Level: {prediction} 😰")
                else:
                    st.error(f"### Predicted Stress Level: {prediction} 😫")
                
                # Probability distribution
                prob_df = pd.DataFrame({
                    'Stress Level': st.session_state['model'].classes_,
                    'Probability': probabilities * 100
                })
                
                fig = px.bar(prob_df, x='Stress Level', y='Probability',
                            title='Prediction Confidence',
                            labels={'Probability': 'Probability (%)'},
                            color='Probability',
                            color_continuous_scale='RdYlGn_r')
                st.plotly_chart(fig, use_container_width=True)
                
                # Recommendations
                st.markdown("---")
                st.subheader("💡 Personalized Recommendations")
                
                if prediction in ['High', 'Very High']:
                    st.error("""
                    **Your stress levels appear elevated. Here are some suggestions:**
                    - 😴 Try to get more sleep (aim for 7-9 hours)
                    - 🏃 Increase physical activity
                    - 📱 Reduce screen time, especially before bed
                    - 🧘 Practice relaxation techniques like meditation
                    - 👥 Spend more time with friends and family
                    - ✅ Break down tasks into smaller, manageable chunks
                    """)
                elif prediction == 'Moderate':
                    st.info("""
                    **Your stress levels are moderate. Consider these tips:**
                    - ⚖️ Maintain work-life balance
                    - 💪 Keep up with regular exercise
                    - 🌙 Ensure consistent sleep schedule
                    - ☕ Monitor caffeine intake
                    - 🎯 Prioritize important tasks
                    """)
                else:
                    st.success("""
                    **Great job! Your stress levels are low. Keep it up!**
                    - ✅ Continue your healthy habits
                    - 🎉 Maintain your current lifestyle
                    - 🌟 Share your wellness strategies with others
                    - 💯 Stay consistent with sleep and exercise
                    """)
    
    with tab3:
        st.subheader("📊 Model Performance Metrics")
        
        if 'model' not in st.session_state:
            st.warning("⚠️ Please train the model first in the 'Model Training' tab!")
        else:
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Model Accuracy", f"{st.session_state['accuracy']*100:.2f}%")
            with col2:
                st.metric("Model Type", "Random Forest")
            with col3:
                st.metric("Test Samples", len(st.session_state['y_test']))
            
            st.markdown("---")
            
            # Confusion Matrix
            cm = confusion_matrix(st.session_state['y_test'], st.session_state['y_pred'])
            
            fig = px.imshow(cm,
                           labels=dict(x="Predicted", y="Actual", color="Count"),
                           x=st.session_state['model'].classes_,
                           y=st.session_state['model'].classes_,
                           title='Confusion Matrix - How Well Does Our Model Predict?',
                           color_continuous_scale='Blues',
                           text_auto=True)
            st.plotly_chart(fig, use_container_width=True)
            
            st.info("""
            **Understanding the Confusion Matrix:**
            - Diagonal cells (top-left to bottom-right) show correct predictions
            - Off-diagonal cells show misclassifications
            - Darker colors indicate higher counts
            - Perfect predictions would show dark diagonal cells only
            """)
            
            st.markdown("---")
            
            # Classification Report
            st.subheader("📋 Detailed Classification Report")
            
            report = classification_report(st.session_state['y_test'], 
                                          st.session_state['y_pred'],
                                          output_dict=True)
            
            report_df = pd.DataFrame(report).transpose()
            report_df = report_df.round(3)
            
            st.dataframe(report_df, use_container_width=True)
            
            st.markdown("""
            **Metrics Explained:**
            - **Precision**: When the model predicts a stress level, how often is it correct?
            - **Recall**: Of all actual cases of a stress level, how many did the model catch?
            - **F1-Score**: Harmonic mean of precision and recall (balanced metric)
            - **Support**: Number of actual occurrences of each class in the test data
            """)

# Conclusion Page
def conclusion_page(df):
    st.title("📝 Conclusion & Key Takeaways")
    st.markdown("### What We Learned About Mental Health and Lifestyle")
    
    st.markdown("---")
    
    # Key Statistics
    st.subheader("📊 Summary Statistics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Avg Sleep Hours", f"{df['sleep_hours'].mean():.2f}h")
        st.metric("Avg Mood Score", f"{df['mood_score'].mean():.2f}/10")
    
    with col2:
        st.metric("Avg Stress Level", f"{df['stress_level'].mean():.2f}/10")
        st.metric("Avg Exercise", f"{df['exercise_minutes'].mean():.0f} min")
    
    with col3:
        st.metric("Avg Screen Time", f"{df['screen_time'].mean():.2f}h")
        st.metric("Avg Social Time", f"{df['social_hours'].mean():.2f}h")
    
    with col4:
        st.metric("Avg Fatigue", f"{df['fatigue_level'].mean():.2f}/10")
        st.metric("Avg Coffee", f"{df['coffee_cups'].mean():.1f} cups")
    
    st.markdown("---")
    
    # Key Findings
    st.subheader("🎯 Key Findings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 💤 Sleep is Crucial
        Our analysis shows that adequate sleep (7-9 hours) is strongly associated with:
        - Higher mood scores
        - Lower stress levels
        - Reduced fatigue
        - Better overall mental health
        
        **Action Item:** Prioritize consistent sleep schedules
        """)
        
        st.markdown("""
        ### 🏃 Exercise Matters
        Regular physical activity correlates with:
        - Reduced stress levels
        - Improved mood
        - Better stress management
        - Enhanced overall wellbeing
        
        **Action Item:** Aim for at least 30 minutes of daily exercise
        """)
        
        st.markdown("""
        ### 🥗 Diet Quality Impacts Mental Health
        Better nutrition is linked to:
        - Higher mood scores
        - Lower stress levels
        - Better energy levels
        - Improved mental clarity
        
        **Action Item:** Focus on balanced, nutritious meals
        """)
    
    with col2:
        st.markdown("""
        ### 📱 Screen Time Balance
        Excessive screen time is associated with:
        - Increased fatigue
        - Higher stress levels
        - Disrupted sleep patterns
        - Lower mood scores
        
        **Action Item:** Limit screen time, especially before bed
        """)
        
        st.markdown("""
        ### 👥 Social Connections
        Social interaction shows positive correlation with:
        - Better mood scores
        - Lower stress levels
        - Improved emotional wellbeing
        - Enhanced life satisfaction
        
        **Action Item:** Make time for meaningful social connections
        """)
        
        st.markdown("""
        ### ⚖️ Work-Life Balance
        Managing tasks and interruptions helps:
        - Reduce stress levels
        - Improve focus
        - Enhance productivity
        - Better mental health
        
        **Action Item:** Set boundaries and prioritize tasks effectively
        """)
    
    st.markdown("---")
    
    st.subheader("💡 Evidence-Based Recommendations")
    
    st.success("""
    ### For Better Mental Health:
    
    1. **Sleep Hygiene** 🌙
       - Maintain consistent sleep schedule
       - Aim for 7-9 hours nightly
       - Create a relaxing bedtime routine
    
    2. **Physical Activity** 🏃
       - Exercise for at least 30 minutes daily
       - Include both cardio and strength training
       - Find activities you enjoy
    
    3. **Digital Wellness** 📱
       - Limit screen time to reasonable hours
       - Take regular breaks from devices
       - Use blue light filters in the evening
    
    4. **Nutrition** 🥗
       - Eat balanced, nutritious meals
       - Stay hydrated
       - Limit caffeine and processed foods
    
    5. **Social Connection** 👥
       - Make time for friends and family
       - Join communities with shared interests
       - Practice active listening and empathy
    
    6. **Stress Management** 🧘
       - Practice mindfulness or meditation
       - Use time management techniques
       - Seek support when needed
    """)
    
    st.markdown("---")
    
    if 'accuracy' in st.session_state:
        st.subheader("🤖 Machine Learning Model Summary")
        
        st.info(f"""
        Our Random Forest model achieved **{st.session_state['accuracy']*100:.2f}% accuracy** 
        in predicting stress levels based on lifestyle factors. This demonstrates that:
        
        - Lifestyle choices have measurable impacts on mental health
        - Machine learning can help identify patterns in wellbeing
        - Personalized interventions can be data-driven
        - Early identification of stress risk factors is possible
        """)
    
    st.markdown("---")
    
    st.subheader("🌟 Final Thoughts")
    
    st.markdown("""
    Mental health is influenced by numerous interconnected factors. While our analysis provides 
    valuable insights, remember that:
    
    - **Everyone is unique** - What works for one person may differ for another
    - **Professional help matters** - Don't hesitate to seek professional support when needed
    - **Small changes add up** - Gradual lifestyle improvements can make a big difference
    - **Consistency is key** - Sustainable habits are better than drastic changes
    - **Be patient** - Mental health improvement takes time and effort
    
    This dashboard provides a data-driven perspective on mental health, but always consult 
    healthcare professionals for personalized advice.
    """)
    
    st.success("Thank you for exploring this Mental Health Analytics Dashboard! 🧠💚")
    
    st.markdown("---")
    
    st.markdown("""
    <div style='text-align: center; color: #7f8c8d;'>
        <p>Dashboard created as part of Data Science & Machine Learning project</p>
        <p>Data analysis performed using Python, Pandas, Scikit-learn, and Plotly</p>
    </div>
    """, unsafe_allow_html=True)

# Main App Logic
def main():
    try:
        df = load_data()
    except FileNotFoundError:
        st.error("⚠️ Data file not found! Please ensure 'synthetic_mental_health_dataset__1_.csv' is in the same directory as this app.")
        st.stop()
    
    # Navigation
    page = sidebar_navigation()
    
    if page == "🏠 Home":
        home_page()
    elif page == "📊 Dataset Overview":
        dataset_overview_page(df)
    elif page == "📈 EDA & Insights":
        eda_insights_page(df)
    elif page == "🤖 Prediction Model":
        prediction_model_page(df)
    elif page == "📝 Conclusion":
        conclusion_page(df)

if __name__ == "__main__":
    main()
