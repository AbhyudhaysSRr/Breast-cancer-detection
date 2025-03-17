# Breast Cancer Detection

## Overview
This project aims to build a machine learning model for the detection of breast cancer. The project focuses on using a variety of machine learning techniques to predict whether a tumor is malignant or benign based on features extracted from the breast cancer dataset. The main goal is to develop an effective and efficient model that can assist healthcare professionals in making informed decisions.

The project uses various machine learning algorithms such as Logistic Regression, Support Vector Machines (SVM), and others to train on the dataset. The entire pipeline is designed to help understand the workflow of deploying a machine learning model for a real-world healthcare application.

## Features
- Data preprocessing to clean and prepare the dataset for modeling.
- Model training using multiple machine learning algorithms.
- Hyperparameter tuning for optimizing model performance.
- Deployment of the final model using `MLflow` for experiment tracking.
- Deployment of the model using `Joblib` and AWS for real-time predictions.

## Dataset
The dataset used in this project is the famous Breast Cancer Wisconsin dataset, available in the UCI Machine Learning Repository. The dataset contains features like the radius, texture, perimeter, area, and smoothness of the tumor cells.

- **Dataset source**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic))
  
You can also access the dataset in the project folder.

## Technologies Used
- **Python**: The primary programming language.
- **Scikit-learn**: For implementing machine learning algorithms.
- **MLflow**: For experiment tracking and managing machine learning models.
- **Joblib**: For saving the trained model and loading it for deployment.
- **AWS**: For deploying the model in a cloud environment.
- **Pandas**: For data manipulation and preprocessing.
- **Matplotlib / Seaborn**: For data visualization.

## Installation

### Clone the repository:
```bash
git clone https://github.com/AbhyudhaysSRr/Breast-cancer-detection.git
cd Breast-cancer-detection
