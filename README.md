## Table of Contents

1. [What is Streamlit](#What-is-Streamlit?)
2. [Why should data scientists use streamlit](#Why-should-data-scientists-use-streamlit)
3. [Tools](#Tools)
4. [Display Texts with Streamlit](#Display-Texts-with-Streamlit)
5. [Display an Image Video or Audio File](#Display-an-Image-Video-or-Audio-File)
6. [Input Widgets](#Input-Widgets)
7. [Example](#Example)
8. [How to Run the App](#How-to-Run-the-App)

## What is Streamlit

Streamlit is a free and open-source framework to rapidly build and share beautiful machine learning and data science web apps. It is a python-based library specifically designed for machine learning engineers. 

Data scientists or machine learning engineers are not web developers and they're not interested in spending weeks learning to use these frameworks to build webs. Instead, they want a tool that is easier to learn and to use, as long as it can display data and collect needed parameters for modeling.

## Why should data scientists use streamlit

You don't need to know the basics of web  development to get started or to create your first web applocation. So if you're into data science and you want to deploy your model easily, quickly, and with only few lines of code, Streamlit is a good fit.

Streamlit is the easiest way especially for people with no front-end-knowledge to put their code into a web application.

  * No front-end (html, js, css) experience/ knowledge required.
  * You can create a really beautiful ML or DS app in only a few hours or minutes.
  * Less code is requires to create amaizing web apps.
  * It is compatible with the majority of python librarie (eg. pandas, matplotlib, seaborn, plotly, keras, pytorch)

## Tools

* **Python:** Programming language
* **VsCode:** IDE

## Display Texts with Streamlit

```python
import streamlit as st

st.title("This is the app title")
st.header("This is the header")
st.markdown("This is the markdown")
st.subheader("This is the subheader")
st.caption("This is the caption")
st.code("x = 2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')
```

## Display an Image Video or Audio File

You can't find functions as easy as Streamlit functions to display images, videos, and audio files.

```python
st.image("kid.jpg", caption="A kid playing")
st.audio("audio.mp3")
st.video("video.mp4")
```
**Note:** If your media files are in the same directory as your python script, you can just use the file names directly.

## Input Widgets

Widgets are the most important user interface components.

```python
st.checkbox('Yes')
st.button('Click Me')
st.radio('Pick your gender', ['Male', 'Female'])
st.selectbox('Pick a fruit', ['Apple', 'Banana', 'Orange'])
st.multiselect('Choose a planet', ['Jupiter', 'Mars', 'Neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0, 50)
```

## Example

The main profit of loans comes directly from the loan's interest. The loan companies grant a loan after an intensive process of verification and validation. However, they still don't have assuarance if the applicant is able to repay the loan with no difficulties. I will build a simple predictive model (Random Forest Classifier) to predict the loan status of an applicant.

## Objective:

Prepare a web app to make the predictive model available for production.

## Data

The loan dataset used in this example had only 7 columns:
* Gender
* Loan_amount
* Rate of interest
* Income
* Credit_score
* term
* status

## How to Run the App

Run this command in the VsCode terminal:

```streamlit run example.py```


