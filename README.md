## Table of Contents

1. [What is Streamlit](#What-is-Streamlit?)
2. [Why should data scientists use streamlit](#Why-should-data-scientists-use-streamlit)
3. [Tools](#Tools)
4. [Display Texts with Streamlit](#Display-Texts-with-Streamlit)
5. [Display an Image Video or Audio File](#Display-an-Image-Video-or-Audio-File)
6. [Input Widgets](#Input-Widgets)
7. [Display Progress and Status](#Display-Progress-and-Status)
8. [Sidebar and Container](#Sidebar-and-Container)
9. [Creating Multiple Pages](#Creating-Multiple-Pages)
10. [Example](#Example)
11. [How to Run the App](#How-to-Run-the-App)
12. [Resources](#Resources)

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

**Note:** `st.selectbox` allows users to select a single option from a dropdown list while `st.multiselect` allows users to select multiple options from a list.

```python
st.number_input('Pick a number', 0, 10)
st.text_input('Email address')
st.date_input('Traveling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')
```

## Display Progress and Status

Progress bars

```python
st.balloons()  # Celebration balloons
st.progress(10)  # Progress bar
with st.spinner('Wait for it...'):
    time.sleep(10)  # Simulating a process delay
```

Status messages
```python
st.success("You did it!")
st.error("Error occurred")
st.warning("This is a warning")
st.info("It's easy to build a Streamlit app")
st.exception(RuntimeError("RuntimeError exception"))
```

## Sidebar and Container

This help to organize your app. The hierarchy and arrangement of pages on your app can have a large impact on your user experience. By organizing your content you allow visitors to unnderstand and navigate your site, which helps them find what the're looking for and increases the likelihood that they'll return in the future.

### Sidebar

Passing an element to `st.sidebar()` will make this element pinned to the left, allowing users to focus on the content in your app. This will make your app more organized and easier to understand.

```python
st.sidebar.title("Sidebar Title")
st.sidebar.markdown("This is the sidebar content")
```

### Container

`st.container()` is used to create an invisible container where you can put elements in order to create a useful arrangement and hierarchy.

```python
with st.container():
    st.write("This is inside the container")
```

## Creating Multiple Pages

In the directory where the python file is situated, create a new folder named **pages**. Users have to name that folder pages as Streamlit will not understand any other directory name.

To add content in the pages we simply write code on those Python files by importing streamlit and using it’s methods.

Streamlit by default order our pages alphabetically, we can change that by making changes in the file name by adding a specific number infront of their name followed by an underscore like this –

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

## Resources

A [link](https://www.datacamp.com/tutorial/streamlit?utm_source=google&utm_medium=paid_search&utm_campaignid=19589720824&utm_adgroupid=157156376311&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=716160943561&utm_targetid=aud-1645446892440:dsa-2218886984100&utm_loc_interest_ms=&utm_loc_physical_ms=9208973&utm_content=&utm_campaign=230119_1-sea~dsa~tofu_2-b2c_3-row-p2_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na-oct24&gad_source=1&gclid=CjwKCAjwyfe4BhAWEiwAkIL8sJlCN6OAFQUkLz7XG_gpttnza_RpC745GdsxnKk4hcPapFMxYm44vxoCpTwQAvD_BwE) to datacamp website on building streamlit app.


