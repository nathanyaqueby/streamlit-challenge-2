"""
Nathanya Queby Satriani
18/04/2023
"""

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

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

def convert_excel(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_excel().encode('utf-8')

# sidebar
st.sidebar.header("1. Visualization Type 🖼️")
st.sidebar.markdown("""
Select the type of visualization you want to see.
""")
viz_type = st.sidebar.multiselect("Visualization Type", ("Pie Chart", "Bar Chart", "Line Chart"), ("Pie Chart", "Bar Chart", "Line Chart"))

# select which column to focus on when generating the visualization
st.sidebar.header("2. Focus Column 📌")
st.sidebar.markdown("""
Select the column you want to focus on when generating the visualization.
""")
focus_column = st.sidebar.selectbox("Focus Column", ("Expense", "Details", "Recipient", "Date", "Amount"))


# create a dataframe
df = pd.DataFrame({
    "Expense": ["Rent", "Food", "Transportation", "Phone", "Other", "Food", "Transportation"],
    "Details": ["Monthly rent", "Groceries", "Gas, Uber, etc.", "Phone bill", "Charity", "Groceries", "Gas, Uber, etc."],
    "Recipient": ["Landlord", "Grocery Store", "Gas Station", "Phone Company", "Charity", "Grocery Store", "Gas Station"],
    "Date": ["01/12/2021", "02/12/2021", "03/12/2021", "04/12/2021", "05/12/2021", "06/12/2021", "07/12/2021"],
    "Payment Method": ["Debit", "Cash", "Cash", "Credit", "Cash", "Cash", "Cash"],
    "Amount": [1000, 400, 200, 50, 300, 400, 200]
},
index=[i for i in range(1, 8)]
)

edited_df = st.experimental_data_editor(df, use_container_width=True, num_rows="dynamic", )

# download the dataframe as a csv file
st.sidebar.header("3. Download Dataframe 📥")
st.sidebar.markdown("""
Download the dataframe as a csv or excel file.
""")
file_type = st.sidebar.radio("Download as", ("CSV", "Excel"), horizontal=True)

if file_type == "CSV":
    file = convert_df(edited_df)
elif file_type == "Excel":
    file = convert_excel(edited_df)

st.sidebar.download_button("Download dataframe", file, "expense_report.csv", "text/csv")

# create tabs depending on the visualization type
if "Pie Chart" in viz_type:
    st.header("Pie Chart 🥧")
    st.markdown("""
    This is a pie chart.
    """)
    fig = px.pie(edited_df, values="Amount", names=focus_column, title=f"{focus_column} Pie Chart")
    st.plotly_chart(fig)
if "Bar Chart" in viz_type:
    st.header("Bar Chart 📊")
    st.markdown("""
    This is a bar chart.
    """)
    fig = px.bar(edited_df, x=focus_column, y="Amount", title=f"{focus_column} Bar Chart")
    st.plotly_chart(fig)
if "Line Chart" in viz_type:
    st.header("Line Chart 📈")
    st.markdown("""
    This is a line chart.
    """)
    fig = px.line(edited_df, x=focus_column, y="Amount", title=f"{focus_column} Line Chart")
    st.plotly_chart(fig)

# footer
st.markdown("""
---
Made by [Nathanya Queby Satriani](https://linkedin.com/in/queby/)
""")