Salary Prediction using Linear Regression

📌 Project Overview

This project explores the Salary Prediction Data dataset using Linear Regression to model the relationship between an individual's years of experience and their salary. The goal is to build a predictive model that can accurately estimate salaries based on experience.

📊 Dataset Information

Dataset Name: Salary Prediction Data

Source: Kaggle - Salary Prediction Data

Features:

YearsExperience: Number of years of work experience

Salary: Salary of the individual (target variable)

🎯 Project Objectives

Perform Exploratory Data Analysis (EDA) to understand the dataset.

Visualize relationships between experience and salary.

Apply Linear Regression to predict salaries.

Evaluate model performance using metrics like RMSE, R² score, and MAE.

🛠️ Technologies Used

Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)

Jupyter Notebook / Google Colab

Linear Regression (Supervised Learning Model)

📁 Project Structure

├── data/                   # Folder containing dataset
│   ├── salary_data.csv      # Salary dataset
├── notebooks/               # Jupyter notebooks
│   ├── 01_EDA.ipynb         # Exploratory Data Analysis
│   ├── 02_Modeling.ipynb    # Linear Regression Model
├── README.md                # Project Documentation
├── requirements.txt         # Required libraries

🔎 Exploratory Data Analysis (EDA)

Checked for missing values and outliers

Visualized relationships using scatter plots and histograms

Identified correlations between variables

📈 Model Development

Split the dataset into training and testing sets (80/20 split).

Fitted a Linear Regression Model using sklearn.linear_model.LinearRegression.

Evaluated Model Performance:

Mean Squared Error (MSE)

R² Score

Mean Absolute Error (MAE)

🚀 Results & Findings

The model showed a strong positive correlation between YearsExperience and Salary.

R² Score: XX.XX (indicating the percentage of variance explained by the model)

Predictions were reasonably accurate, making this a good candidate for salary forecasting.

📌 How to Run the Project

Clone this repository:

git clone https://github.com/yourusername/salary-prediction.git

Navigate to the project folder:

cd salary-prediction

Install dependencies:

pip install -r requirements.txt

Open Jupyter Notebook and run notebooks/02_Modeling.ipynb.

📢 Future Improvements

Apply Polynomial Regression for better accuracy.

Incorporate additional features (e.g., job roles, industries).

Deploy the model using Streamlit or Flask for real-time predictions.

🤝 Contributing

Contributions are welcome! Feel free to fork the repo, make enhancements, and submit a pull request.

📩 Contact

For any questions, reach out via:
📧 Email: ronnymuthomi254@gmail.com🔗 LinkedIn: 

⭐ If you find this project useful, don't forget to star the repository!

