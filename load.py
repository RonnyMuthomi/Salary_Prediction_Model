import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("Salary_prediction_model.pkl")  # Ensure correct path

# Set page config
st.set_page_config(layout="wide")

# Sidebar - Model info
with st.sidebar:
    st.title("💡 About the Model")
    st.markdown("""
    - **Purpose**: Predict Salary  
    - **Dataset**: [https://www.kaggle.com/datasets/mrsimple07/salary-prediction-data](#)  
    - **Model Used**: Decision Tree Regressor  
    - **Developer**: Ronny M 
    """)

# Two-column layout
col1, col2 = st.columns(2)

with col1:
    st.header("🔢 Enter Input Parameters")

    # Dropdowns for categorical variables
    education = st.selectbox("Education Level", ["High School", "Bachelor's", "Master's", "PhD"])
    job_title = st.selectbox("Job Title", ["Data Analyst", "Software Engineer", "Manager", "HR"])
    location = st.selectbox("Location", ["New York", "San Francisco", "Los Angeles", "Chicago"])
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])

    # Number inputs for numerical values
    experience = st.number_input("Years of Experience", min_value=0, max_value=50, value=5)
    age = st.number_input("Age", min_value=18, max_value=70, value=30)

    # Auto-calculate 'Years Until Retirement'
    retirement_age = 65
    years_until_retirement = max(retirement_age - age, 0)

    # Convert categorical data to numerical (for model input)
    education_map = {"High School": 0, "Bachelor's": 1, "Master's": 2, "PhD": 3}
    job_map = {"Data Analyst": 0, "Software Engineer": 1, "Manager": 2, "HR": 3}
    location_map = {"New York": 0, "San Francisco": 1, "Los Angeles": 2, "Chicago": 3}
    gender_map = {"Male": 0, "Female": 1, "Other": 2}

    # Prepare final input data (Ensure 16 features are used)
    input_data = np.array([
        education_map[education],
        job_map[job_title],
        location_map[location],
        gender_map[gender],
        experience,
        age,
        years_until_retirement
    ] + [0] * 9).reshape(1, -1)  # Add placeholders for remaining features

with col2:
    st.header("📊 Prediction Output")

    if st.button("Predict Salary"):
        predicted_salary = model.predict(input_data)[0]
        st.success(f"💰 Predicted Salary: ${predicted_salary:,.2f}")

# Footer
st.markdown("""
---
🔗 **Made with Streamlit** | 🛠 **Developed by Ronny M**
""", unsafe_allow_html=True)
