"""
===========================================================
Project : Human Development Index (HDI) Predictor
Internship : AIML Internship Project
Module : Machine Learning Model Training
Author : Ampolu Raj Kumar & Team
Description :
    This script loads the cleaned HDI dataset, preprocesses
    the data, trains a Linear Regression model, evaluates
    its performance, and saves the trained model using Pickle.
===========================================================
"""

# ==========================================================
# Import Required Libraries
# ==========================================================

import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    r2_score,
    mean_squared_error,
    mean_absolute_error
)

# ==========================================================
# Step 1: Load the Cleaned Dataset
# ==========================================================

print("=" * 60)
print("Loading Cleaned Dataset...")
print("=" * 60)

df = pd.read_csv("dataset/clean_hdi.csv")

print("\nDataset Loaded Successfully!\n")

# Display first five records
print(df.head())

# Display dataset information
print("\nDataset Shape :", df.shape)
print("\nDataset Columns :")
print(df.columns)

# ==========================================================
# Step 2: Select Features (Independent Variables)
# ==========================================================

print("\n" + "=" * 60)
print("Selecting Features and Target Variable")
print("=" * 60)

# Features used for prediction
X = df[
    [
        "LifeExpectancy",
        "ExpectedSchooling",
        "MeanSchooling",
        "GNI"
    ]
]

# Target variable (HDI Score)
y = df["HDI"]

print("\nSelected Features:")
print(X.head())

print("\nTarget Variable:")
print(y.head())

# ==========================================================
# Step 3: Split Dataset into Training and Testing Data
# ==========================================================

print("\n" + "=" * 60)
print("Splitting Dataset")
print("=" * 60)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Dataset Shape :", X_train.shape)
print("Testing Dataset Shape  :", X_test.shape)

# ==========================================================
# Step 4: Train the Machine Learning Model
# ==========================================================

print("\n" + "=" * 60)
print("Training Linear Regression Model")
print("=" * 60)

model = LinearRegression()

model.fit(X_train, y_train)

print("\nModel Training Completed Successfully!")

# ==========================================================
# Step 5: Predict HDI Values
# ==========================================================

print("\n" + "=" * 60)
print("Predicting HDI Scores")
print("=" * 60)

y_pred = model.predict(X_test)

print("\nFirst 10 Predicted HDI Scores:\n")
print(y_pred[:10])

# ==========================================================
# Step 6: Evaluate Model Performance
# ==========================================================

print("\n" + "=" * 60)
print("Model Evaluation")
print("=" * 60)

# Calculate evaluation metrics
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"R² Score               : {r2:.4f}")
print(f"Mean Squared Error     : {mse:.6f}")
print(f"Mean Absolute Error    : {mae:.6f}")

# ==========================================================
# Step 7: Save the Trained Model
# ==========================================================

print("\n" + "=" * 60)
print("Saving Trained Model")
print("=" * 60)

model_path = "model/hdi_model.pkl"

with open(model_path, "wb") as file:
    pickle.dump(model, file)

print(f"\nModel Saved Successfully!")
print(f"Location : {model_path}")

# ==========================================================
# Project Completed
# ==========================================================

print("\n" + "=" * 60)
print("HDI Predictor Model Training Completed Successfully!")
print("=" * 60)