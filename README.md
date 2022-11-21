# Bank-Customer-Churn-Analysis

## Introduction
We aim to accomplish the following for this study.

1) Identify and visualize which factors contribute to customer churn:

2) Build a prediction model that will perform the following:

 - Classify if a customer is going to churn or not.
 - Preferably and based on model performance, choose a model that predicts the churn to make it easier for customer service to target low hanging fruits in their efforts to prevent churn.

3) Build an app to predict whether a customer going to churn or not depeneding on a set of details.

## About the Data
The dataset has been obtained from kaggle. The following are the list of features in the dataset:
 - CreditScore          int64
 - Geography           object
 - Gender              object
 - Age                  int64
 - Tenure               int64
 - Balance            float64
 - NumOfProducts        int64
 - HasCrCard            int64
 - IsActiveMember       int64
 - EstimatedSalary    float64
 - Exited               int64
 
### Analysing the dataset
The following shows the proportion of customer churned and retained:

![image](https://user-images.githubusercontent.com/85822284/199734710-2eb46262-fd38-4dac-9112-4a356c2a6620.png)

#### SMOTE
Since there is an imbalance in dataset. SMOTE has been used for balancing. Synthetic Minority Oversampling Technique (SMOTE) is a statistical technique for increasing the number of cases in your dataset in a balanced way. The component works by generating new instances from existing minority cases that you supply as input. This implementation of SMOTE does not change the number of majority cases.

## Machine Learning Models
Different machine learning models have been used to find out the best model out of it. The following are the ML models used:
 - Logistic Regression
 - SVC
 - KNNeighbours Classifier
 - Decision Tree Classifier
 - Random forest Classifier
 - Gradient Boosting Classifier
 
Out of these, AUC-ROC(Area Under The Curve - Receiver Operating Characteristics) has been taken to finalise **Random Forest Classifier** as the best model which has a score of about **85%**. Comparison of AUC-ROC score for all of these models:

![image](https://user-images.githubusercontent.com/85822284/203001006-f6bf139f-0317-441d-93d2-9302c18aa805.png)


## Feature Importance
Feature importance refers to techniques that assign a score to input features based on how useful they are at predicting a target variable.

![image](https://user-images.githubusercontent.com/85822284/199744934-e9761802-d321-4676-9d6e-257cdf143684.png)

 - Feature: 0, Score: 0.11445
 - Feature: 1, Score: 0.23109
 - Feature: 2, Score: 0.07144
 - Feature: 3, Score: 0.12260
 - Feature: 4, Score: 0.10195
 - Feature: 5, Score: 0.01937
 - Feature: 6, Score: 0.10721
 - Feature: 7, Score: 0.12362
 - Feature: 8, Score: 0.01517
 - Feature: 9, Score: 0.02767
 - Feature: 10, Score: 0.06543
 
 From the above scores, we can finalise that Geography is one of the important feature in this model followed by number of products the customer has with the bank.


## Churn Predictor App:
![Untitled](https://user-images.githubusercontent.com/85822284/199740901-87c9652d-f552-4afd-b17f-bae2d4d2806d.png)

This is an user friendly and easily customizable app that predicts whether the customer is going to churn or not with the given set of details about the customer. This app is created with the help of Streamlit.
This app will ask the following details about the customer for prediction:
 - Credit Score
 - Age
 - Loan Tenure
 - Available Balance
 - Number of products
 - Availability of Credit Cards
 - Whether the customer is active
 - Estimated Salary
 - Location
 - Gender
 
 ## Conclusion
 Although the model has good AUC-ROC score, down the line it can be improved by:
  - Adding more data
  - Feature Selection.
 
