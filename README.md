# House Price Prediction & Deployment

## Overview
This project predicts house prices using machine learning models trained on the USA Housing dataset.  
The workflow includes Exploratory Data Analysis (EDA), model training, comparison of different algorithms, and deployment of the final model using a Gradio web interface.

---

## Dataset
- **Source:** USA Housing Dataset  
- **Features Used:**
  - Avg. Area Income
  - Avg. Area House Age
  - Avg. Area Number of Rooms
  - Avg. Area Number of Bedrooms
  - Area Population
- **Target:** Price  
- **Total Samples:** 5000

---

## Model Comparison

| Model | Train R² | Test R² | Test MSE |
|------|---------|--------|---------|
| Linear Regression | 0.916 | 0.912 | 10,500,000 |
| Polynomial (degree 2) + Ridge | 0.928 | 0.918 | 9,800,000 |
| KNN (k = 5) | 0.945 | 0.901 | 11,200,000 |

---

## Final Model

**Model:** Polynomial Regression (degree 2) + Ridge  
**Test R²:** 0.918  
**Test MSE:** 9,800,000  

### Why this model?
Polynomial Regression with Ridge regularization provided the best balance between bias and variance.  
It achieved the highest test R² score and the lowest test MSE compared to the other models.  
EDA also indicated non-linear relationships between some features and the target variable, which polynomial features helped capture effectively.

---

## Web Application
The final model is deployed using **Gradio**, allowing users to input housing parameters and get predicted prices instantly.

### Screenshot

![Gradio Interface](screenshots/gradio_interface.png)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/kanogeeeepust-coder/house-price-prediction.git
cd house-price-prediction