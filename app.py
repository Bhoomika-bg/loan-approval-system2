import streamlit as st  # import streamlit library for building UI

from ao_star import evaluate_loan  # import AO* evaluation function from ao_star module


st.title("🏦 Loan Approval using AO* Algorithm")  # set the title of the application


income = st.number_input(  # create input field for income
    "Monthly Income ($)",  # label shown to user
    min_value=1000,  # minimum allowed income
    max_value=1000000,  # maximum allowed income
    value=None,  # no default value (removes initial 0)
    step=1000  # increment step when increasing value
)


credit_score = st.number_input(  # create input field for credit score
    "Credit Score",  # label shown to user
    min_value=300,  # minimum valid credit score
    max_value=850,  # maximum valid credit score
    value=None  # no default value
)


dti = st.number_input(  # create input field for DTI ratio
    "DTI Ratio (%)",  # label shown to user
    min_value=1,  # minimum DTI
    max_value=100,  # maximum DTI
    value=None  # no default value
)


loans = st.number_input(  # create input field for existing loans
    "Existing Loans",  # label shown to user
    min_value=0,  # minimum loans
    max_value=10,  # maximum loans allowed
    value=None  # no default value
)


loan_amount = st.number_input(  # create input field for loan amount
    "Loan Amount ($)",  # label shown to user
    min_value=5000,  # minimum loan amount
    max_value=1000000,  # maximum loan amount
    value=None,  # no default value
    step=5000  # increment step
)


if st.button("Evaluate (AO*)"):  # create a button to trigger evaluation


    if None in [income, credit_score, dti, loans, loan_amount]:  # check if any field is empty
        st.error("⚠️ Please fill all fields")  # show error message if inputs are missing


    elif loan_amount > income * 20:  # check if loan amount is too high compared to income
        st.warning("⚠️ Loan amount is too high compared to income")  # show warning message


    else:  # execute if all validations pass

        decision, cost, explanation = evaluate_loan(  # call AO* function
            income,  # pass income
            credit_score,  # pass credit score
            dti,  # pass DTI
            loans,  # pass number of loans
            loan_amount  # pass loan amount
        )


        st.subheader(f"Decision: {decision}")  # display final decision


        st.write(f"Total Cost: {cost}")  # display calculated cost


        st.write("### Explanation:")  # display explanation header


        for e in explanation:  # loop through explanation list
            st.write("-", e)  # display each explanation item
