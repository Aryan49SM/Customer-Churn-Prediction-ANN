import streamlit as st
import numpy as np
import tensorflow as tf
import pandas as pd
import pickle

def main():
    st.title("💼 Customer's Salary Prediction")
    st.write("Please enter the customer details below:")

    # Load the trained model and encoders
    model = tf.keras.models.load_model('Regression/regression_model.h5')
    with open('onehot_encoder_geo.pkl', 'rb') as file:
        onehot_encoder_geo = pickle.load(file)
    with open('label_encoder_gender.pkl', 'rb') as file:
        label_encoder_gender = pickle.load(file)
    with open('Regression/scaler_regression.pkl', 'rb') as file:
        scaler = pickle.load(file)

    col1, col2 = st.columns(2)
    
    with col1:
        geography = st.selectbox('Geography', onehot_encoder_geo.categories_[0])
        gender = st.selectbox('Gender', label_encoder_gender.classes_)
        credit_score = st.number_input('Credit Score', min_value=0)
        age = st.slider('Age', 18, 92)
        balance = st.number_input('Balance', min_value=0.0, format="%.2f")

    with col2:
        exited = st.selectbox('Exited', [0, 1])
        tenure = st.slider('Tenure', 0, 10)
        num_of_products = st.slider('Number of Products', 1, 4)
        has_cr_card = st.selectbox('Has Credit Card', [0, 1])
        is_active_member = st.selectbox('Is Active Member', [0, 1])

    if st.button("Predict Salary"):

        input_data = pd.DataFrame({
            'CreditScore': [credit_score],
            'Gender': [label_encoder_gender.transform([gender])[0]],
            'Age': [age],
            'Tenure': [tenure],
            'Balance': [balance],
            'NumOfProducts': [num_of_products],
            'HasCrCard': [has_cr_card],
            'IsActiveMember': [is_active_member],
            'Exited': [exited]
        })

        # One-hot encode 'Geography'
        geo_encoded = onehot_encoder_geo.transform([[geography]]).toarray()
        geo_encoded_df = pd.DataFrame(geo_encoded, columns=onehot_encoder_geo.get_feature_names_out(['Geography']))
        input_data = pd.concat([input_data.reset_index(drop=True), geo_encoded_df], axis=1)

        # Scale the input data
        input_data_scaled = scaler.transform(input_data)

        # Predict salary
        prediction = model.predict(input_data_scaled)
        predicted_salary = prediction[0][0]

        st.info(f'Predicted Estimated Salary: **${predicted_salary:.2f}**')
