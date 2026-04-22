import streamlit as st  # import streamlit for UI creation

from ao_star import evaluate_loan  # import AO* evaluation function from ao_star file

st.title("🏦 Loan Approval using AO* Algorithm")  # set title of the web app

income = st.number_input("Applicant Income ($)", 0)  # take income input from user
credit_score = st.number_input("Credit Score", 0)  # take credit score input
dti = st.number_input("DTI Ratio (%)", 0)  # take debt-to-income ratio input
loans = st.number_input("Existing Loans", 0)  # take number of existing loans
loan_amount = st.number_input("Loan Amount ($)", 0)  # take loan amount input

if st.button("Evaluate (AO*)"):  # create button to trigger evaluation

    decision, cost, explanation = evaluate_loan(  # call AO* function with inputs
        income, credit_score, dti, loans, loan_amount  # pass all user inputs
    )

    st.subheader(f"Decision: {decision}")  # display final decision (Approve/Reject/Review)

    st.write(f"Total Cost: {cost}")  # display calculated cost (risk score)

    st.write("### Explanation:")  # heading for explanation section

    for e in explanation:  # loop through explanation list
        st.write("-", e)  # display each explanation point