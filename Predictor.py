# -----------------------------------------Importing Packages--------------------------------------

import joblib
import streamlit as st
from streamlit_lottie import st_lottie
import json
import requests

# -----------------------------------------Importing Packages--------------------------------------

con = st.container()

head = con.header('Customer Details:')

# ------------Expander----------------
exp = con.expander('Details to be filled')
credit_score = exp.number_input(label = 'Provide Credit Score', min_value= 300, max_value= 900)
Age = exp.number_input(label = 'Age', min_value = 18, max_value = 70)
tenure = exp.number_input(label = 'Loan Tenure', min_value=0, max_value= 40)
balance = exp.number_input(label = 'Available Balance')
Num_products = exp.number_input(label = 'Number of Products')

Crd = exp.selectbox('Availability of Credit Card?', ('yes', 'no'))
if Crd == 'yes':
    CreditCard = 1
else:
    CreditCard = 0

act = exp.selectbox('Is the customer active?', ('yes', 'no'))
if act == 'yes':
    actmember = 1
else:
    actmember = 0

salary = exp.number_input('Estimated Salary?')

g = exp.selectbox('Location', ('France', 'Germany', 'Spain'))
if g == 'France':
    one = 0
    two = 0
elif g == 'Germany':
    one = 1
    two = 0
else:
    one = 0
    two = 1

gen = exp.selectbox('Gender', ('Male', 'Female'))
if gen == 'Male':
    gender = 1
else:
    gender = 0

predict = exp.button('Predict')

# -------------------Expander------------------

# -----------------------------------------Model Loading-----------------------------------------

def predictor():
    model = joblib.load('Churn_Predict_Model')
    result = model.predict([[credit_score, Age, tenure, balance, Num_products, CreditCard, actmember, salary, one, two, gender]])

    if result == [1]:
        def lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()

        lottie_ani = lottieurl('https://assets2.lottiefiles.com/datafiles/reG36xPQqtlCUR0/data.json')
        ani = st_lottie(lottie_ani, key="hello")
        anim = con.ani1
        subh = con.subheader('Oops, the customer is gonna be churned. Kindly contact the customer')

    else:
        def lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()

        lottie_ani2 = lottieurl('https://assets1.lottiefiles.com/packages/lf20_jnw2bd4s.json')
        ani2 = st_lottie(lottie_ani2, key="hello2")
        anim2 = con.ani2
        subh2 = con.subheader('Great, the customer will not be churned')

if predict:
    predictor()

# -----------------------------------------Model Loading-----------------------------------------