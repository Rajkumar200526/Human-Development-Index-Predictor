# 🌍 Human Development Index (HDI) Predictor

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?logo=bootstrap)
![License](https://img.shields.io/badge/License-MIT-green)

### AI & Machine Learning Internship Project

Predict the **Human Development Index (HDI)** of countries using **Machine Learning**, **Flask**, and **Data Visualization**.

</div>

---

# 📖 Project Overview

The **Human Development Index (HDI) Predictor** is an end-to-end Machine Learning web application that predicts a country's Human Development Index based on four important development indicators:

- ❤️ Life Expectancy
- 🎓 Expected Years of Schooling
- 📚 Mean Years of Schooling
- 💰 Gross National Income (GNI) Per Capita

The project includes data preprocessing, exploratory data analysis (EDA), model training using Linear Regression, and deployment through a Flask web application.

---

# 🚀 Features

- 📊 Data Cleaning & Preprocessing
- 📈 Exploratory Data Analysis (EDA)
- 🤖 Linear Regression Model
- 🎯 HDI Score Prediction
- 🌍 Country Selection
- 🖥️ Flask Web Application
- 🎨 Responsive Bootstrap 5 UI
- 📉 Correlation Heatmap
- 📊 Distribution & Scatter Plots
- 💾 Pickle Model Serialization

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | Data Analysis |
| NumPy | Numerical Computing |
| Matplotlib | Data Visualization |
| Seaborn | Statistical Visualization |
| Scikit-learn | Machine Learning |
| Flask | Web Framework |
| Bootstrap 5 | Responsive Frontend |
| HTML5 | Web Pages |
| CSS3 | Styling |
| JavaScript | Interactivity |
| Pickle | Model Serialization |
| Git & GitHub | Version Control |

---

# 📂 Project Structure

```text
HDI_Predictor/
│
├── dataset/
│   ├── hdi.csv
│   └── clean_hdi.csv
│
├── graphs/
│   ├── boxplot.png
│   ├── correlation_matrix.png
│   ├── gni_hdi.png
│   ├── hdi_distribution.png
│   ├── life_hdi.png
│   ├── pairplot.png
│   ├── school_hdi.png
│   └── stripplot.png
│
├── model/
│   └── hdi_model.pkl
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   ├── script.js
│   │   └── autofill.js
│   └── images/
│
├── templates/
│   ├── index.html
│   ├── predict.html
│   └── result.html
│
├── app.py
├── eda.py
├── visualization.py
├── preprocessing.py
├── train_model.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📊 Dataset Features

The model is trained using the following features:

| Feature | Description |
|----------|-------------|
| Country | Country Name |
| Life Expectancy | Average Life Expectancy |
| Expected Schooling | Expected Years of Schooling |
| Mean Schooling | Mean Years of Schooling |
| GNI | Gross National Income Per Capita |
| HDI | Human Development Index Score |

---

# 🧠 Machine Learning Workflow

```
Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Feature Selection
      │
      ▼
Train-Test Split
      │
      ▼
Linear Regression Model
      │
      ▼
Model Evaluation
      │
      ▼
Pickle Serialization
      │
      ▼
Flask Web Application
```

---

# 📈 Exploratory Data Analysis

The project includes:

- Distribution Plot
- Scatter Plot
- Correlation Matrix
- Heatmap
- Pair Plot
- Strip Plot
- Box Plot

---

# 🎯 Model Evaluation

The model is evaluated using:

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)

---

# 🖥️ Web Application

The Flask application includes:

- 🏠 Home Page
- 🌍 Country Selection
- 📝 HDI Prediction Form
- 📊 Prediction Result Page
- 📱 Responsive Design

---

# ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/Rajkumar200526/Human-Development-Index-Predictor.git
```

Go to the project folder:

```bash
cd Human-Development-Index-Predictor
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

# 📸 Screenshots

Add screenshots here after deployment.

Example:

```
screenshots/
│
├── home.png
├── prediction.png
└── result.png
```

---

# 🌐 Deployment

The project can be deployed using:

- Render
- Railway
- PythonAnywhere

---

# 👨‍💻 Developer

**Ampolu Raj Kumar**

AI & Machine Learning Enthusiast

GitHub:
https://github.com/Rajkumar200526

---

# 🎓 Internship Project

This project was developed as part of an **Artificial Intelligence & Machine Learning Internship** to demonstrate:

- Machine Learning
- Data Analysis
- Flask Web Development
- Data Visualization
- Model Deployment

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

## Thank You ❤️