# -----------------------------------------Importing Packages--------------------------------------
import joblib
import streamlit as st
from streamlit_lottie import st_lottie
import json
import requests
# -----------------------------------------Importing Packages--------------------------------------

# --------------------------------------------Page Layout-------------------------------------------

st.set_page_config(
    page_title= 'Churn Predictor'
)

con = st.container()
side = st.sidebar

def lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_ani = lottieurl('https://assets9.lottiefiles.com/packages/lf20_EHugAD.json')
ani = st_lottie(lottie_ani, key = "hello")

title = con.title('Customer Churn Predictor')
anim = con.ani
head = con.header('This Churn predictor will predict whether the customer with given set of details will churn or not.')

# --------------------------------------------Page Layout-------------------------------------------


