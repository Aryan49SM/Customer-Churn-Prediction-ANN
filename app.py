import streamlit as st
import src.classification_app as classification
import src.regression_app as regression

def main():
    st.set_page_config(page_title="Customer Insights App", layout="wide")
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("", ["Customer Churn Prediction", "Customer's Salary Prediction"])

    if selection == "Customer Churn Prediction":
        classification.main()
    else:
        regression.main()

if __name__ == "__main__":
    main()
