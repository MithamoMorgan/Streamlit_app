# Import necessary library
import streamlit as st

# Add a title
st.title("Dairy Farmer's portal:cow:")

# Add a radio buttom
st.radio("Are you a dairy farmer?", ('yes', 'no'))

# input text
st.text_input("Enter Farmer's ID", "fam4934/2020")

# Slider
st.slider("Year of registration", 2010, 2024)

# Pick gender
st.selectbox("Pick your gender", ['Male', 'Female'])

# Number
st.number_input("Number of cows", 0,500)

# dropdown
st.selectbox("Enter Region", ['Central', 'South', 'West'])

# Text area
st.text_area("A short description of yourself")