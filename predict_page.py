import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()
regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def show_predict_page():
    st.markdown(
        """
        <style>
        .main {
            padding-top: 1rem;
        }
        .salary-card {
            text-align: center;
            background: #f0f8ff;
            border-radius: 20px;
            padding: 30px;
            margin-top: 20px;
            box-shadow: 0px 4px 15px rgba(0, 191, 255, 0.3);
        }
        .salary-text {
            font-size: 42px;
            color: #0077b6;
            font-weight: bold;
        }
        .sub-salary {
            font-size: 24px;
            color: gray;
            margin-top: -10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### Enter Your Details")

    countries = (
        'Australia', 'Brazil', 'Canada', 'France', 'Germany', 'India', 'Italy',
        'Netherlands', 'Spain', 'Sweden', 'Ukraine',
        'United Kingdom of Great Britain and Northern Ireland',
        'United States of America',
    )

    education = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
    )

    col1, col2 = st.columns(2)
    with col1:
        country = st.selectbox("Country", countries)
    with col2:
        education_level = st.selectbox("Education Level", education)

    experience = st.slider("Years of Experience", 0, 50, 0)

    col_center = st.columns([1, 1.2, 1])[1]
    with col_center:
        ok = st.button("Predict Salary", use_container_width=True)

    if ok:
        X = np.array([[country, education_level, experience]])

        try:
            X[:, 0] = le_country.transform(X[:, 0])
            X[:, 1] = le_education.transform(X[:, 1])
        except ValueError as e:
            st.error(f"Error: Could not process input. {e}")
            return

        X = X.astype(float)
        salary = regressor.predict(X)

        USD_TO_INR = 84.0
        salary_usd = salary[0]
        salary_inr = salary_usd * USD_TO_INR

        st.markdown(
            f"""
            <div class="salary-card">
                <div class="salary-text">${salary_usd:,.0f} / year</div>
                <div class="sub-salary">≈ ₹{salary_inr:,.0f} INR</div>
                <p style="font-size:16px; color:gray;">(Based on 1 USD ≈ {USD_TO_INR} INR)</p>
            </div>
            """,
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    show_predict_page()
