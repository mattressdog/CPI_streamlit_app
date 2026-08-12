import pandas as pd
import numpy as np
import streamlit as st

#page_1 = st.Page("pages/page_one.py", title="CPI Graph")
#pg = st.navigation([page_1])
#pg.run()

st.set_page_config(page_title="CPI Visualizer", page_icon="📈", layout="centered")

# Page setup

st.title("CPI Data")
st.write("Upload your dataset or view the demo sample below.")

# Sidebar options
st.sidebar.header("Data Settings")
use_sample = st.sidebar.checkbox("Use sample dataset", value=True)

df = None

if use_sample:
    
    df = pd.read_csv("historical-cpi-u-202606.csv")



else:
    # File uploader for user CSV
    uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        # Select numeric columns to plot
        numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns.tolist()
        if numeric_cols:
            selected_cols = st.sidebar.multiselect(
                "Select columns to plot", numeric_cols, default=numeric_cols[:2]
            )
            df = df[selected_cols]

st.dataframe(df)

salary = st.number_input("Enter a sallary:", value=0, step=1)

beginning_year = st.selectbox("Select beginning year:", df.iloc[:, 0].unique())
beginning_year_row = df[df.iloc[:, 0] == beginning_year].index.tolist()
end_year = st.selectbox("Select ending year:", df.iloc[:, 0].unique())
end_year_row = df[df.iloc[:, 0] == end_year].index.tolist()
Select_month = st.selectbox("Select month:", df.columns[1:14].tolist())
month_col_number = df.columns.get_loc(Select_month)


if st.button("Run"):
    beginning_value = df.iloc[beginning_year_row, month_col_number].item()
    end_value = df.iloc[end_year_row, month_col_number].item()
    inflate_rate = ((end_value - beginning_value)/beginning_value)*100
    new_salary = salary*(end_value/beginning_value)
    
    
    st.write("Running script...")


    st.write(beginning_year, end_year, Select_month )

    st.write("inflation Rate: ")
    #st.write(beginning_value, end_value)
    st.write(inflate_rate)
    st.write("A Salary in ", end_year, " of ", new_salary, " has the same purchasing power as a salary in " , beginning_year, " of " , salary, " dollars.")

