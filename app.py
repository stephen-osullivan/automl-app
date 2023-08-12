import streamlit as st
# run with: $ streamlit run app.py
x = st.slider("Select a value")
st.write(x, "squared is", x * x)