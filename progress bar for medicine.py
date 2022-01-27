import streamlit as st
import pandas as pd
import numpy as np
import time
import datetime
import math

st.title("**Zarmed Pratiksha**")
but = st.button("Bosing")
# 1-bar:
text = st.sidebar.text_input("Bemor1:")
t = st.number_input(f"{text}ning operatsiya jarayoni:")
my_bar = st.progress(0)
completion = st.empty()
# 2-bar:
text1 = st.sidebar.text_input("Bemor2:")
t1 = st.number_input(f"{text1}ning operatsiya jarayoni: ")
my_bar1 = st.progress(0)
completion1 = st.empty()
# 3-bar:
text2 = st.sidebar.text_input("Bemor3:")
t2 = st.number_input(f"{text2}ning operatsiya jarayoni:  ")
my_bar2 = st.progress(0)
completion2 = st.empty()
if but:
    for i in range(101):
        time.sleep(t*60/101)  # -(t1*60/101)-(t2*60/101)
        completion.text("%i%% Tugadi" % i)
        my_bar.progress(i)
        time.sleep(t1*60/101)  # -t2*60/101
        completion1.text("%i%% Tugadi" % i)
        my_bar1.progress(i)
        time.sleep(t2*60/101)
        completion2.text("%i%% Tugadi" % i)
        my_bar2.progress(i)
