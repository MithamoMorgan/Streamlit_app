# Import necessary libraries
import streamlit as st
import pandas as pd
import joblib

# Load the saved model
random_forest_model = joblib.load('random_forest_model.pkl')

# Function for making predictions
def predict_status(input_data):
    # Predict using the loaded model
    prediction = random_forest_model.predict(input_data)
    return prediction

# Streamlit app title
st.title("Loan Default Prediction App")

# Gender selection (with corresponding numeric values)
gender = st.selectbox('Gender', ('Not available', 'Male', 'Female', 'Joint'))

# Convert the selected value to the corresponding numeric code
if gender == 'Not available':
    gender = 3
elif gender == 'Male':
    gender = 1
elif gender == 'Female':
    gender = 2
else:
    gender = 4

# Numeric inputs for other fields
loan_amount = st.number_input('Loan Amount', min_value=0)
rate_of_interest = st.number_input('Rate of Interest', min_value=0.0)
income = st.number_input('Income', min_value=0)
credit_score = st.number_input('Credit Score', min_value=0)
term = st.number_input('Term', min_value=0)

# Prepare the input data in the correct format (this must match your model’s input format)
input_data = pd.DataFrame({
    'Gender': [gender],
    'loan_amount': [loan_amount],
    'rate_of_interest': [rate_of_interest],
    'income': [income],
    'Credit_Score': [credit_score],
    'term': [term]})

# Display the prediction when the button is clicked
if st.button('Predict Loan Status'):
    result = predict_status(input_data)
    st.write(f'Predicted Loan Status: {"Defaulted" if result == 1 else "Not Defaulted"}')