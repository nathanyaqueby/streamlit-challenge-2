import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Expense Tracker",
                   page_icon="💰",
                   layout="wide",
                   initial_sidebar_state="expanded",
                   menu_items={
                       'Get Help': "mailto:nathanyaqueby21@gmail.com",
                       'Report a bug': "mailto:nathanyaqueby21@gmail.com",
                       'About': "An expense tracker app made with Streamlit."
                       })

# description
st.markdown("""
# Expense Tracker
This app is used to track your expenses and visualize them. 
Select the type of visualization you want to see using the sidebar. 
Insert your expenses in the dataframe below and click on the button to generate the visualization.
""")

# sidebar
st.sidebar.header("Visualization Type")
st.sidebar.markdown("""
Select the type of visualization you want to see.
""")
viz_type = st.sidebar.selectbox("Visualization Type", ("Pie Chart", "Bar Chart", "Line Chart"))

# dataframe
st.header("Insert your expenses")

# create a dataframe
df = pd.DataFrame({
    "Expense": ["Rent", "Food", "Transportation", "Phone", "Other"],
    "Amount": [1000, 400, 200, 50, 300]
})

edited_df = st.experimental_data_editor(df)

# generate visualization from the edited dataframe
if st.button("Generate Visualization"):
    if viz_type == "Pie Chart":
        fig = px.pie(edited_df, values="Amount", names="Expense", title="Expense Pie Chart")
        st.plotly_chart(fig)
    elif viz_type == "Bar Chart":
        fig = px.bar(edited_df, x="Expense", y="Amount", title="Expense Bar Chart")
        st.plotly_chart(fig)
    elif viz_type == "Line Chart":
        fig = px.line(edited_df, x="Expense", y="Amount", title="Expense Line Chart")
        st.plotly_chart(fig)

# footer
st.markdown("""
---
Made by [Nathanya Queby Satriani](https://linkedin.com/in/queby/)
""")