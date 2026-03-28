import streamlit as st
import requests

st.title("💰 AI Loan Assistant")

income = st.number_input("Income")
credit_score = st.number_input("Credit Score")
loan_amount = st.number_input("Loan Amount")

if st.button("Check Loan"):
    response = requests.post(
        "http://127.0.0.1:8000/analyze",
        json={
            "income": income,
            "credit_score": credit_score,
            "loan_amount": loan_amount
        }
    )
    st.write(response.json())