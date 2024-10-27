## Table of Contents

1. [What is Streamlit](#What-is-Streamlit?)
2. [Why should data scientists use streamlit](Why-should-data-scientists-use-streamlit)
3. [Example](#Example)

## What is Streamlit

Streamlit is a free and open-source framework to rapidly build and share beautiful machine learning and data science web apps. It is a python-based library specifically designed for machine learning engineers. 

Data scientists or machine learning engineers are not web developers and they're not interested in spending weeks learning to use these frameworks to build webs. Instead, they want a tool that is easier to learn and to use, as long as it can display data and collect needed parameters for modeling.

## Why should data scientists use streamlit

You don't need to know the basics of web  development to get started or to create your first web applocation. So if you're into data science and you want to deploy your model easily, quickly, and with only few lines of code, Streamlit is a good fit.

It is compatible with the majority of python librarie (eg. pandas, matplotlib, seaborn, plotly, keras, pytorch)

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

## Limitations
* The data used for the prediction had few columns, which may lead to inaccurate predictions due to insufficient features for the model to learn from.
* The file random_forest_model.pkl was not pushed to this repository due to its large size and was added to the .gitignore file

## App
### Without user input:
![](https://github.com/MithamoMorgan/Streamlit_app/blob/master/Imgs/before_img.jpg)

### With User Input/predicted:
![](https://github.com/MithamoMorgan/Streamlit_app/blob/master/Imgs/after_img.jpg)


