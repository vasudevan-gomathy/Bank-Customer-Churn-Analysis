# ---------------------------------------Importing Packages----------------------------------------
import pandas as pd
import numpy as np
import joblib
import streamlit as st
from streamlit_lottie import st_lottie
import json
import requests
import matplotlib.pyplot as plt
import joblib

# ---------------------------------------Importing Packages----------------------------------------

# ---------------------------------------Front End----------------------------------------


report = st.container()

title = report.title('Report')
txt = report.subheader('Kindly upload CSV file for generating report')
uploaded_file = report.file_uploader("Choose a file")


# ---------------------------------------Back End (PIPELINE)----------------------------------------
if uploaded_file:

    # 1) Data Collection:

    df = pd.read_csv(uploaded_file)

    # 2) Data Engineering:

    df.dropna(how='any', inplace=True)
    df = df.drop(['RowNumber', 'CustomerId', 'Surname', 'Exited'], axis=1)
    df = pd.get_dummies(df, drop_first=True)

    # 3) Prediction:

    model = joblib.load('Churn_Predict_Model')
    result = model.predict(df)

    # 4) Result:

    df.insert(11, "Result", result, True)



    def convert_df(df):
        return df.to_csv().encode('utf-8')

    csv = convert_df(df)

    st.download_button(
        label="Download Report as CSV",
        data=csv,
        file_name='Report.csv',
        mime='text/csv',
    )

    # 5) Report:
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    x, y = df['Result'].value_counts()
    labels = 'Customer not Churned', 'Customer Churned'
    sizes = [x, y]
    # explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)



