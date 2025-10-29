import streamlit as st
from predict_page import show_predict_page

st.set_page_config(
    page_title="Developer Salary Predictor",
    page_icon="💰",
    layout="centered"
)

# Modern styled header
st.markdown(
    """
    <h1 style='text-align: center; color: #00BFFF;'>💻 Software Developer Salary Predictor</h1>
    <p style='text-align: center; color: gray; font-size: 18px;'>
        Get an estimated salary based on your country, education, and experience.
    </p>
    <hr>
    """,
    unsafe_allow_html=True
)

show_predict_page()
